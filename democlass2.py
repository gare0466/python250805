#나는  개발자 클래서를 정의
class BankAccount:
    #초기화 매서드
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 

    #입금 매서드
    def deposit(self, amount):
        self.balance += amount 

    #출금 매서드
    def withdraw(self, amount):
        self.balance -= amount
        #결과를 출력
        if self.balance < 0:
            print("잔액이 부족합니다.")

    #문자열 표현 매서드
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, self.name, self.balance)
    
    #인스턴스 2개를 생성하고 싶어
account1 = BankAccount(100, "전우치", 15000)
account2 = BankAccount(101, "이순신", 20000)        
#출금 테스트
account1.withdraw(3000)
#출력
print(account1)
#출금 테스트
account2.withdraw(25000)        
#출력
print(account2)
# BankAccount.py    
# BankAccount.py    
# BankAccount.py    
