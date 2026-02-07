import re
import time
import html
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
from pathlib import Path
from datetime import datetime

# =========================
# 설정
# =========================
OUT_DIR = Path("naver_scrap_site")  # 결과 폴더
BASE = "https://news.naver.com"

SECTION_URLS = {
    "101_경제": "https://news.naver.com/section/101",
    "102_사회": "https://news.naver.com/section/102",
    "103_생활문화": "https://news.naver.com/section/103",
    "104_세계": "https://news.naver.com/section/104",
    "105_IT과학": "https://news.naver.com/section/105",
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.8",
    "Referer": "https://news.naver.com/",
}

# =========================
# 유틸
# =========================
def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())

def fetch(url: str) -> str:
    with requests.Session() as s:
        r = s.get(url, headers=HEADERS, timeout=12, allow_redirects=True)
        r.raise_for_status()
        return r.text

def is_naver_article_url(url: str) -> bool:
    # 네이버 뉴스 기사 상세는 대개 n.news.naver.com/mnews/article/oid/aid 형태
    return ("n.news.naver.com" in url and "/article/" in url) or ("news.naver.com" in url and "read.naver" in url)

def normalize_to_mnews(url: str) -> str:
    """
    read.naver?oid=..&aid=.. or 기타 형태 -> mnews/article/oid/aid 로 정규화 시도
    실패하면 원본 url 그대로 반환.
    """
    if "n.news.naver.com" in url and "/article/" in url:
        return url

    try:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        oid = (qs.get("oid") or [""])[0]
        aid = (qs.get("aid") or [""])[0]
        if oid and aid:
            return f"https://n.news.naver.com/mnews/article/{oid}/{aid}"
    except Exception:
        pass

    # 링크가 이미 mnews로 리다이렉트되는 경우도 있으니 그대로 반환
    return url

def pick_first_attr(el, attrs):
    if not el:
        return ""
    for a in attrs:
        v = el.get(a, "")
        if v:
            return v
    return ""

# =========================
# 1) 섹션에서 기사 링크 수집
# =========================
def extract_links_from_section(section_url: str, limit: int = 12):
    html_text = fetch(section_url)
    soup = BeautifulSoup(html_text, "html.parser")

    # 섹션 페이지에서 기사 블록 후보들
    blocks = soup.select("li.sa_item, div.sa_itm_flex, div.sa_item_flex")
    seen = set()
    results = []

    for b in blocks:
        a = b.select_one("a.sa_text_title") or b.select_one(".sa_text_strong") or b.select_one("a")
        if not a:
            continue
        href = a.get("href", "")
        if not href:
            continue
        href = urljoin(BASE, href)

        # 중복 제거
        if href in seen:
            continue
        seen.add(href)

        # 기본 타이틀(섹션에서 잡히는 것) - 원문 스크랩 실패 대비
        title = ""
        title_el = b.select_one(".sa_text_strong") or b.select_one(".sa_text_title")
        if title_el:
            title = norm(title_el.get_text())

        press = ""
        press_el = b.select_one(".sa_text_press") or b.select_one("em.sa_text_press") or b.select_one(".press")
        if press_el:
            press = norm(press_el.get_text())

        thumb = ""
        img = b.select_one("img")
        if img:
            thumb = pick_first_attr(img, ["data-src", "data-original", "src"])
            thumb = urljoin(BASE, thumb) if thumb else ""

        results.append({
            "section_list_title": title,
            "section_list_press": press,
            "section_list_thumb": thumb,
            "link": href,
        })

        if len(results) >= limit:
            break

    return results

# =========================
# 2) 기사 원문에서 제목/신문사/대표이미지 스크랩
# =========================
def scrape_article_meta(article_url: str):
    """
    원문(가능하면 네이버 기사)에서:
    - title: og:title or #title_area
    - press: 로고 alt or 기타 텍스트
    - image: og:image 우선
    """
    u = normalize_to_mnews(article_url)
    html_text = fetch(u)
    soup = BeautifulSoup(html_text, "html.parser")

    # 대표 이미지: og:image 우선
    og_img = soup.select_one('meta[property="og:image"]')
    image = og_img.get("content", "").strip() if og_img else ""

    if not image:
        # fallback: 본문 이미지 중 첫 번째
        body_img = soup.select_one("#dic_area img") or soup.select_one(".end_photo_org img") or soup.select_one(".article_photo img")
        if body_img:
            image = pick_first_attr(body_img, ["data-src", "data-original", "src"]).strip()

    # 제목: og:title 우선
    og_title = soup.select_one('meta[property="og:title"]')
    title = norm(og_title.get("content", "")) if og_title else ""
    if not title:
        title_el = soup.select_one("#title_area") or soup.select_one("h2#title_area") or soup.select_one("h1")
        title = norm(title_el.get_text()) if title_el else ""

    # 신문사: 로고 alt 우선
    press = ""
    logo = soup.select_one(".media_end_head_top_logo img[alt]") or soup.select_one(".media_end_head_top_logo img")
    if logo:
        press = norm(logo.get("alt", ""))

    if not press:
        # fallback: 상단 영역 텍스트에서 뽑기
        press_el = soup.select_one(".media_end_head_top_logo") or soup.select_one(".media_end_head_top")
        press = norm(press_el.get_text()) if press_el else ""

    # 너무 길게 잡히면 첫 토큰만(안전)
    if len(press) > 30:
        press = press.split()[0]

    return {
        "title": title,
        "press": press,
        "image": image,
        "canonical": u,  # 실제 스크랩한 URL(정규화된 URL)
    }

# =========================
# 3) HTML 생성
# =========================
CSS = """
:root{
  --bg:#0b0f14; --panel:#121a24; --panel2:#0f1620; --border:#1f2a38;
  --text:#e8eef6; --muted:#9fb0c3; --accent:#7dd3fc;
  --r16:16px;
}
*{box-sizing:border-box}
body{
  margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
  background:var(--bg); color:var(--text);
}
a{color:inherit; text-decoration:none}
a:hover{text-decoration:underline}
.container{max-width:1100px; margin:0 auto; padding:22px}
.header{
  border-bottom:1px solid rgba(31,42,56,.8);
  background:rgba(11,15,20,.88);
  position:sticky; top:0; z-index:10;
  backdrop-filter: blur(10px);
}
.header-inner{max-width:1100px; margin:0 auto; padding:14px 22px; display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap;}
h1{margin:0; font-size:18px}
.sub{margin:4px 0 0; color:var(--muted); font-size:12px}
.btn{
  display:inline-block; padding:10px 12px; border-radius:999px;
  border:1px solid rgba(31,42,56,.9); background:rgba(18,26,36,.7);
  font-size:12px;
}
.btn:hover{border-color: rgba(125,211,252,.35); text-decoration:none}
.grid-btns{display:grid; grid-template-columns: repeat(auto-fill, minmax(200px,1fr)); gap:12px; margin-top:18px;}
.bigbtn{
  padding:16px 14px; border-radius:16px; border:1px solid rgba(31,42,56,.9);
  background:rgba(18,26,36,.86);
  display:flex; flex-direction:column; gap:8px;
}
.bigbtn .t{font-weight:800}
.bigbtn .d{color:var(--muted); font-size:12px}
.bigbtn:hover{border-color: rgba(125,211,252,.35); text-decoration:none}

.cards{display:grid; grid-template-columns: repeat(auto-fill, minmax(320px,1fr)); gap:14px; margin-top:16px;}
.card{
  border:1px solid rgba(31,42,56,.9); border-radius:16px; overflow:hidden;
  background:rgba(18,26,36,.86);
}
.thumb{
  height:170px; background:rgba(15,22,32,.85);
  display:flex; align-items:center; justify-content:center;
}
.thumb img{width:100%; height:100%; object-fit:cover; display:block}
.noimg{color:var(--muted); font-size:12px}
.body{padding:12px 12px 14px; display:flex; flex-direction:column; gap:10px}
.title{
  font-weight:800; font-size:14px; line-height:1.35;
  display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;
}
.meta{display:flex; justify-content:space-between; align-items:center; gap:10px}
.press{
  color:var(--muted); font-size:12px; max-width:70%;
  white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
  border:1px solid rgba(31,42,56,.8); background:rgba(15,22,32,.6);
  padding:4px 10px; border-radius:999px;
}
.badge{
  font-size:11px; color:var(--accent);
}
.note{color:var(--muted); font-size:12px; margin-top:14px}
"""

def build_index_html(all_sections):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    buttons = []
    for name, meta in all_sections.items():
        file = meta["file"]
        cnt = meta["count"]
        buttons.append(f"""
        <a class="bigbtn" href="{html.escape(file)}">
          <div class="t">{html.escape(name)}</div>
          <div class="d">스크랩 {cnt}건 보기</div>
        </a>
        """)

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>네이버 섹션 스크랩(101~105)</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="header-inner">
      <div>
        <h1>네이버 섹션 스크랩 (101~105)</h1>
        <div class="sub">생성: {now} · 버튼을 눌러 섹션별 스크랩 결과 확인</div>
      </div>
      <div>
        <a class="btn" href="https://news.naver.com/" target="_blank" rel="noopener noreferrer">네이버 뉴스</a>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="grid-btns">
      {''.join(buttons)}
    </div>
    <div class="note">
      * 각 섹션 페이지는 “원문(네이버 기사)”에서 제목/신문사/대표이미지를 다시 추출해 표시합니다. 추출 실패 시 섹션 목록 정보로 대체됩니다.
    </div>
  </div>
</body>
</html>
"""

def build_section_html(section_name, section_url, items):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cards = []
    for it in items:
        title = html.escape(it.get("title") or it.get("fallback_title") or "")
        press = html.escape(it.get("press") or it.get("fallback_press") or "")
        img = it.get("image") or it.get("fallback_thumb") or ""
        link = it.get("canonical") or it.get("link") or ""

        img_tag = f'<img src="{html.escape(img)}" alt="thumbnail">' if img else '<div class="noimg">No Image</div>'

        badge = "스크랩됨" if it.get("scraped_ok") else "스크랩 실패(대체표시)"

        cards.append(f"""
        <article class="card">
          <a class="thumb" href="{html.escape(link)}" target="_blank" rel="noopener noreferrer">
            {img_tag}
          </a>
          <div class="body">
            <a class="title" href="{html.escape(link)}" target="_blank" rel="noopener noreferrer">{title}</a>
            <div class="meta">
              <span class="press">{press if press else "언론사 정보 없음"}</span>
              <span class="badge">{badge}</span>
            </div>
          </div>
        </article>
        """)

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(section_name)} 스크랩</title>
  <style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="header-inner">
      <div>
        <h1>{html.escape(section_name)} 스크랩</h1>
        <div class="sub">출처: {html.escape(section_url)} · 생성: {now}</div>
      </div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <a class="btn" href="index.html">← ALL</a>
        <a class="btn" href="{html.escape(section_url)}" target="_blank" rel="noopener noreferrer">섹션 원문</a>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="cards">
      {''.join(cards)}
    </div>
  </div>
</body>
</html>
"""

# =========================
# 메인 실행
# =========================
def run(limit_each: int = 12, delay_sec: float = 0.35):
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    all_sections_meta = {}

    for section_name, section_url in SECTION_URLS.items():
        print(f"[섹션 수집] {section_name} -> {section_url}")
        links = extract_links_from_section(section_url, limit=limit_each)

        scraped_items = []
        for x in links:
            link = x["link"]
            fallback_title = x["section_list_title"]
            fallback_press = x["section_list_press"]
            fallback_thumb = x["section_list_thumb"]

            item = {
                "link": link,
                "fallback_title": fallback_title,
                "fallback_press": fallback_press,
                "fallback_thumb": fallback_thumb,
                "scraped_ok": False,
            }

            # 원문(네이버 기사)에서 스크랩 시도
            try:
                if is_naver_article_url(link):
                    meta = scrape_article_meta(link)
                    item.update(meta)
                    item["scraped_ok"] = True
                else:
                    # 네이버 기사로 정규화가 될 수도 있으니 한번 시도
                    m = normalize_to_mnews(link)
                    if is_naver_article_url(m):
                        meta = scrape_article_meta(m)
                        item.update(meta)
                        item["scraped_ok"] = True
            except Exception:
                pass

            # 표시용 필드(스크랩 성공하면 meta title/press, 실패하면 fallback)
            item["title"] = item.get("title") or fallback_title
            item["press"] = item.get("press") or fallback_press
            item["image"] = item.get("image") or fallback_thumb

            scraped_items.append(item)
            time.sleep(delay_sec)

        # 섹션 페이지 저장
        section_id = section_name.split("_", 1)[0]
        section_file = f"section_{section_id}.html"
        (OUT_DIR / section_file).write_text(
            build_section_html(section_name, section_url, scraped_items),
            encoding="utf-8",
        )

        all_sections_meta[section_name] = {"file": section_file, "count": len(scraped_items)}

    # ALL 페이지 저장 (버튼만)
    (OUT_DIR / "index.html").write_text(build_index_html(all_sections_meta), encoding="utf-8")

    print("\n완료!")
    print("열기:", (OUT_DIR / "index.html").resolve())


if __name__ == "__main__":
    run(limit_each=12)
