#DemoForm2.py
#DemoForm2.ui (화면) + DemoForm2.py (로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import urllib.request
import re

#디장인한 파일을 로딩 (DemoForm2.ui)
form_class = uic.loadUiType("DemoForm.ui")[0]
#DemoForm 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
        self.label.setText("첫번째 문자열 출력 ") # 라벨에 문자열 출력
def firstclick(self):
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
    self.label.setText("첫번째 클릭 이벤트 발생")  # 라벨에 문자열 출력     
def secondclick(self):
    self.label.setText("두번째 클릭 이벤트 발생")
    def thirdclick(self):
        self.label.setText("세번째 클릭 이벤트 발생")

# 진입점을 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    myWindow = DemoForm()  # DemoForm 객체 생성
    myWindow.show()  # 윈도우 표시
    sys.exit(app.exec_())  # 이벤트 루프 시작       