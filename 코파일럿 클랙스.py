class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_classes():
    # 1. Person 객체 생성 및 정보 출력
    p1 = Person(1, "홍길동")
    p1.printInfo()

    # 2. Manager 객체 생성 및 정보 출력
    m1 = Manager(2, "김철수", "팀장")
    m1.printInfo()

    # 3. Employee 객체 생성 및 정보 출력
    e1 = Employee(3, "이영희", "Python")
    e1.printInfo()

    # 4. Manager의 title 변경 후 출력
    m1.title = "부장"
    m1.printInfo()

    # 5. Employee의 skill 변경 후 출력
    e1.skill = "Java"
    e1.printInfo()

    # 6. Person의 name 변경 후 출력
    p1.name = "최길동"
    p1.printInfo()

    # 7. Manager 객체 추가 생성 및 출력
    m2 = Manager(4, "박민수", "과장")
    m2.printInfo()

    # 8. Employee 객체 추가 생성 및 출력
    e2 = Employee(5, "정수진", "C++")
    e2.printInfo()

    # 9. Manager 객체의 id 변경 후 출력
    m2.id = 10
    m2.printInfo()

    # 10. Employee 객체의 name 변경 후 출력
    e2.name = "한지민"
    e2.printInfo()

if __name__ == "__main__":
    test_classes()