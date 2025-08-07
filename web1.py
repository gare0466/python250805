#web1.py
#크롤링 작업
from bs4 import BeautifulSoup

#페이지를 로딩
page = open('chap09_test.html', 'rt', encoding='utf-8')
# 검색 용이한 개체
soup = BeautifulSoup(page, 'html.parser')
#전체문서 보기
# print(soup.prettify())
#<p> 전체 검색
# print(soup.find_all('p'))  # <p> 태그 전체 검색
print(soup.find_all('p', class_='s'))  # class 속성이 s인 <p> 태그 검색
#id = first인 <p> 태그 검색
print(soup.find_all('p', id='first'))  # id 속성이 first인 <p> 태그 검색

for tag in soup.find_all('p'):
    title = tag.text.strip()  # <p> 태그의 텍스트 추출
    title = title.replace('/n', '')  # 줄바꿈 문자 제거
    print(title)  # 텍스트 출력