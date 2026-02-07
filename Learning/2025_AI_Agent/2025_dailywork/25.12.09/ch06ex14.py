import os
# 싸이킷컨 패키지 설치(python을 아나콘다로 설치하면 포함됨)
# pip install scikit-leran (패키지)
# 물결 표시나 빨간줄 표시는 아직 해당 프로그램이 설치되지 않았다는 표시
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 문서 로딩
def load_docs(path="docs"):
    files = os.listdir(path)
    docs = []
    for f in files:
        with open(os.path.join(path, f), "r", encoding="utf-8") as fp:
            data = fp.read()
            docs.append(data)
    return docs

def retrieve(query, docs, top_k=1):
    vect = TfidfVectorizer()
    tfidf = vect.fit_transform([query] + docs)
    scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    idx = scores.argsort()[::-1][:top_k]
    return [docs[i] for i in idx]

# 어플리케이션의 진입점 (Entry point)
if __name__ == "__main__":
    docs = load_docs()
    q = "프로젝트 제출 규칙을 알려줘"
    retrieved = retrieve(q, docs)
    print("[검색된 문서 조각]")
    print(retrieved[0])
