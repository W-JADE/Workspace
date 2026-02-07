import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm 

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = pd.DataFrame({
    "views": [120, 340, 560, 430, 290],
    "comments": [5, 18, 42, 30, 12]
})

plt.scatter(df["views"], df["comments"])


plt.title("조회 수와 댓글 수의 관계")
plt.xlabel("조회 수")
plt.ylabel("댓글 수")

plt.show()
