import requests
from bs4 import BeautifulSoup
import pandas as pd

data_list = []

def fetch_data(url):
    response = requests.get(url)  # 發送請求
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有電影的 infoArea 和 iconArea 區塊
    movies = soup.find_all("section", class_="infoArea")
    icons = soup.find_all("section", class_="iconArea")

    # 使用 zip() 將電影和標記區塊配對
    for movie, icon in zip(movies, icons):
        # 找電影名稱
        name = movie.find("h2").a.text.strip()

        # 找上映日期
        date = movie.find("time").text.strip()

        # 找所有 theaterMark 標記並合併
        marks = (", ".join([
            mark.get_text(strip=True)
            for mark in icon.find_all("span", class_="theaterMark")]) or "N/A")  # 若無標記則設為 "N/A"

        # 將資料加入列表
        data_list.append([name, date, marks])

    # 印出所有抓取到的資料
    for data in data_list:
        print(f"電影名稱: {data[0]}, 上映日期: {data[1]}, 放映版本: {data[2]}")

# 測試網址
url = "https://www.vscinemas.com.tw/vsweb/film/index.aspx"
fetch_data(url)

# 將資料保存為 Excel 文件
df = pd.DataFrame(data_list, columns=["電影名稱", "上映日期", "放映版本"])
df.to_excel("現正熱映.xlsx", index=False, engine="openpyxl")
print("資料已成功保存為 Excel 文件")

