#democlass
#1) 클래스의 정의 
class Person:  # 클래스 이름은 일반적으로 대문자로 시작합니다 (PEP 8 스타일 가이드).
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    def print_name(self): # 메서드 이름이 내장 함수 print와 겹치지 않도록 변경하는 것을 권장합니다.
        print("My name is {0}". format(self.name))
        print(f"My name is {self.name}") # f-string 구문 오류 수정

#2) 인스턴스 생성
p1 = Person() # 정의된 클래스 이름(Person)과 동일하게 수정
p2 = Person()
#3) 메서드 호출 
p1.print_name() # 변경된 메서드 이름으로 호출