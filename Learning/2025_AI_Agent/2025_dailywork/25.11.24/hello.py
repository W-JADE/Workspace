# 1. 가상환경 설정하기 : python -m venv .venv
# 2. hello world 불러오기 

print("Hello world!")
'''
=== 결과 ===
Hello world!
'''

# 3. # ① 명령 프롬프트 실행 : cmd
# ② 새 프로젝트 폴더 생성 : mkdir myproject
# ③ 생성한 폴더로 이동 :cd myproject
# ④ 가상환경 생성 (venv 모듈로 venv 이름의 가상환경 생성) 
#   : python -m venv venv

# 4. 가상환경 비활성화 : deactivate

'''
== 모듈 설치 ==
**pip install -q pandas matplotlib openai
- pandas : 데이터 분석
- matplotlib : 데이터 시각화
- openai : OpenAI API 패키지

== 패키지 리스트 확인 ==
- pip list

== 한번에 설치할 목록이 정해져 있다면! ==
1. requirements.txt 파일을 만들어두기
2. pip install -r requirements.txt (파일 내 모든 모듈 설치)
'''
