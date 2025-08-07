#web.py
from bs4 import BeautifulSoup
import urllib.request
import re
#파일로 저장
f = open("clien.txt", "wt", encoding="utf-8")
for i in range(0, 10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    print(url)

# 함수 체인  메서드 체인 
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
        title = tag.text.strip()  # <span> 태그의 텍스트 추출
        if re.search('아이패드', title):
            print(title)  # 텍스트 출력
        # title = title.replace('\n', '')  # 줄바꿈 문자 제거
        f.write(title + "\n")  # 파일에 텍스트 저장
f.close()
#                     </span>