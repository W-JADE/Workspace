# 막대 그래프(Bar Chart)작성 실습하기

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm 

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.DataFrame({
    "media": ["A신문", "B신문", "C신문", "D신문"],
    "article_count": [25, 40, 15, 30]
})

plt.bar(df["media"], df["article_count"])

plt.title("매체별 기사 수 비교")
plt.xlabel("매체")
plt.ylabel("기사 수")

plt.show()