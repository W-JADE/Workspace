from openai import OpenAI
from dotenv import load_dotenv
from reportlab.pdfgen import canvas
import pandas as pd
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 1. Moderate : 입력 안전성 검수하는 함수로 확인하기
def moderate_input(text : str) -> bool :
    """사용자가 입력한 결과가 안전한지 검사 후 문제 없으면 True로 반환"""
    result = client.moderations.create(
        model="omni-moderation-latest",
        input=text        
    )
    flagged = result.results[0].flagged
    return not flagged

# 2. 멀티포팻 콘텐츠 생성(광고/유튜브/SNS)
def generate_multi_format(prompt : str) -> str :
    """하나의 프롬프트로 광고,유튜브,스크립트,SNS 문구를 한번에 생성"""
    response = client.responses.create(
        model= "gpt-4.1-mini",
        input=f"""
        다음 제품/서비스 설명을 바탕으로 멀티포맷 콘텐츠를 생성하라.

        [설명]
        {prompt}

        [요구사항]
        1) 15초 분량 광고 카피
        2) 유튜브 영상 스크립트(약 1분)
        3) 인스타그램용 짧은 SNS 문구 3개

        각 항목을 번호를 붙여서 구분해서 작성하라.
        """
    )
    return response.output_text
    
# 3. Enbedding 생성 함수(RAG응용)
def create_embedding(text : str) :
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    vector = emb.data[0].embedding
    print(">>Embedding 백터 길이 :", len(vector))
    return vector

# 4. TTS : 텍스트를 음성파일로 저장하는 기능
def text_to_speech(text: str, filename: str = "agent_output.mp3"):
    """텍스트를 음성으로 변환하여 mp3 파일로 저장합니다."""
    speech = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )
    speech.stream_to_file(filename)
    print(f"▶ 음성 파일 생성 완료: {filename}")

# 5. Whisper: 음성 파일을 다시 텍스트로 변환
def speech_to_text(filename: str = "agent_output.mp3") -> str:
    """mp3 음성 파일을 Whisper로 텍스트로 변환합니다."""
    with open(filename, "rb") as audio_file:
        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    print("▶ Whisper 변환 결과:", result.text)
    return result.text

# 6. 메인 흐름: 하나의 파이프라인으로 연결
def main():
    print("=== AI Agent 통합 데모 ===")
    user_prompt = input("제품/서비스를 한 줄로 설명해 보세요:\n> ")

    # 1) 입력 내용 안전성 검사
    if not moderate_input(user_prompt):
        print("⚠ 해당 내용은 정책상 문제가 있어 처리할 수 없습니다.")
        return
    print("▶ Moderation 통과: 계속 진행합니다.")

    # 2) 멀티포맷 콘텐츠 생성
    multi_output = generate_multi_format(user_prompt)
    print("\n[멀티포맷 생성 결과]")
    print(multi_output)

    # 3) Embedding 생성 (벡터 길이만 확인)
    create_embedding(user_prompt)

    # 4) 생성된 멀티포맷 결과를 음성으로 저장(TTS)
    text_to_speech(multi_output, "agent_output.mp3")

    # 5) 저장된 음성을 다시 텍스트로 복원(Whisper)
    speech_to_text("agent_output.mp3")

# 7. 엑셀 파일로 저장하기
content = {
    "형식": ["광고", "유튜브 스크립트", "SNS 카피"],
    "내용": [
        "15초 광고 카피 내용...",
        "1분 분량 유튜브 스크립트...",
        "SNS 홍보 문구 3개..."
    ]
}
df = pd.DataFrame(content)

df.to_excel("output.xlsx", index=False)

print("엑셀 저장 완료 : output.xlsx")

# 8. pdf 파일로 저장하기
text = """AI Agent 결과물 PDF 예시

1) 광고 카피
- ...생성된 내용...

2) 유튜브 스크립트
- ...생성된 내용...

3) SNS 홍보문구
- ...생성된 내용...
"""

file = "output.pdf"
c = canvas.Canvas(file)

# PDF에 줄 단위로 텍스트 작성
for i, line in enumerate(text.split("\n")):
    c.drawString(50, 800 - 18 * i, line)

c.save()
print("PDF 저장 완료:", file)

if __name__ == "__main__":
    main()