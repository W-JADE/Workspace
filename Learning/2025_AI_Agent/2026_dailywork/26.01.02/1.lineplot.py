# 선 그래프(Line Plot) 작성해보기_실습

import matplotlib.pyplot as plt      #pip install matplotlib
import pandas as pd                  #pip install pandas
import matplotlib.font_manager as fm #matplotlib 한글 폰트 불러오는 방법

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.DataFrame({
    "hour" : [9,12,15,18,21],
    "views" : [130,340,550,480,240]
})

plt.plot(df["hour"],df["views"])      #선 그래프 x,y축 

plt.title("시간대별 기사 조회 수")
plt.xlabel("시간")
plt.ylabel("조회 수")

plt.show()                             #출력