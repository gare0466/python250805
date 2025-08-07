#Chap09_클리앙중고장터검색.py
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 
f= open('todayhumor.txt', 'wt', encoding='utf-8')
for n in range(1,11):
        #오늘의 유머 베스트게시판
        url ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        #한글이 깨지는 경우
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('td', attrs={'calss':'subject'})
        # <span class="subject_fixed" data-role="list-subject-text" title="맥북프로 M2 13인치 24/512 실버">
		# 		맥북프로 M2 13인치 24/512 실버
		# </span>
        for item in list:
            try:
                  title = item.find('a').text.strip()
                  if re.search('미국', title):
                        print(title)
                        f.write(title + "\n")
            except:
                   pass     
# <td class="subject">
# <a href="/board/view.php?table=bestofbest&amp;no=480470&amp;s_no=480470&amp;page=1" target="_top">길바닥 낙서</a><span class="list_memo_count_span"> [6]</span>  <span style="margin-left:4px;"><img src="https://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> <span style="color:#999">5일</span></td>
            # title = item.text.strip()
            # print(title)


