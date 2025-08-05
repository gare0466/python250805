#부모클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        
#자식클래스
class Student(Person):
    #덮어 쓰기 (Overriding)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모 클래스의 초기화 매서드를 호출
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기(Overriding)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, Subject: {2}, Student ID: {3})".format(
            self.name, self.phoneNumber, self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "24001")
p.printInfo()
s.printInfo()
# print(p.__dict__)
# print(s.__dict__)
