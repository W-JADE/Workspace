# pandas는 표 형태의 데이터를 다루기 위한 파이썬 라이브러리
# 엑셀처럼 행(ROW)과 열(COLUMN) 로 구성된 데이터를 불러오고,확인하고, 계산하고, 정리하는 기능을 제공
# 모듈 설치 전 python.exe -m pip install --upgrade pip 해서 모듈 최신 버전 설치하기

# Tkinter GUI 모듈 불러오기 (파일 선택 창 pip 생성)
import tkinter as tk
from tkinter import filedialog

# CSV 파일 읽기용 라이브러리
import pandas as pd

# Tkinter 기본 창을 숨기기 (파일 선택 창만 띄우기 위해 필요)
root = tk.Tk()
root.withdraw()

# 파일 선택 대화상자 열기
path = filedialog.askopenfilename(
    title="CSV 파일을 선택하세요",
    filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
)

# 파일을 선택했다면 CSV 읽기 진행
if path:
    df = pd.read_csv(path)              # CSV 파일을 DataFrame으로 읽기
    print("선택 파일:", path)
    print(df.head().to_string(index=False))   # 상위 5행만 깔끔하게 출력
else:
    print("파일을 선택하지 않았습니다.")
