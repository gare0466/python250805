#외부라이브러리 설치 
#cmd 

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4&ackey=1ox978v3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 신문기사 제목 추출
titles = []
for item in soup.select('a.news_tit'):
    title = item.get('title')
    if title:
        titles.append(title)

# 엑셀 파일로 저장
wb = Workbook()
ws = wb.active
ws.title = "NaverNews"
ws.append(["번호", "제목"])

for idx, title in enumerate(titles, 1):
    ws.append([idx, title])

wb.save("naverRsult.xlsx")
print("naverRsult.xlsx 파일로 저장 완료")