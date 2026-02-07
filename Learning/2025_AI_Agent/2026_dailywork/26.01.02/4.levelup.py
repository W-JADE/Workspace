# 그래프를 bar그래프로 응용해서 만들어본 버전

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm 

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.DataFrame({
    "views": [120, 340, 560, 430, 290],
    "comments": [5, 18, 42, 30, 12]
})

df_sorted = df.sort_values("views")

#plt.scatter(df["views"], df["comments"])
plt.plot(df_sorted["views"], df_sorted["comments"], marker="o")


plt.title("조회 수와 댓글 수의 관계")
plt.xlabel("조회 수")
plt.ylabel("댓글 수")

plt.show()
