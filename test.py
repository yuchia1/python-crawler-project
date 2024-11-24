import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 範例資料
data_list = [
    ["Movie A", "2024-11-15", "Digital, IMAX"],
    ["Movie B", "2024-11-07", "Digital"],
    ["Movie C", "2024-10-23", "IMAX, 4DX"],
    ["Movie D", "2024-11-01", "Digital, GC"],
    ["Movie E", "2024-10-10", "4DX"],
]

# 建立 DataFrame
df = pd.DataFrame(data_list, columns=["Name", "Date", "Formats"])

# 將 Date 欄位轉換為日期格式
df['Date'] = pd.to_datetime(df['Date'])

# 繪製條形圖
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='Name', data=df, palette="viridis")
plt.title('Movie Release Dates')
plt.xlabel('Release Date')
plt.ylabel('Movie Name')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()