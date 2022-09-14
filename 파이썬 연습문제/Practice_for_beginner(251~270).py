# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self. sex = sex
#
#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")
#
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self. sex = sex
#
#     def __del__(self):
#         print("나의 죽음을 알리지마라")
#
# # areum = Human("아름" , 25, "여자")
# areum = Human("모름", 0, "모름")
# areum.who()
#
# areum.setInfo("아름", 25, "여자")
# areum.who()
#
# areum.setInfo("아름", 25, "여자")
# del areum
# class Stock:
#     def __init__(self, name, code, per, pbr, dividend):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.dividend = dividend
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code
#
#     def set_per(self, per):
#         self.per = per
#
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#
#     def set_dividend(self, dividend):
#         self.dividend = dividend
#
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)
#
# a = Stock(None, None)  # name과 code 모두 None을 넣음
# a.set_name("삼성전자")
# a.set_code("005930")
# print(a.name)
# print(a.code)

# print(삼성.name)
# print(삼성.get_name())
# print(삼성.code)
# print(삼성.get_code())

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# print(samsung.name)
# print(samsung.code)
# print(samsung.per)
# print(samsung.pbr)
# print(samsung.dividend)
#
# samsung.set_per(12.75)
# print("수정 후:",samsung.per)

# Samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# Hyundea = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
#
# 종목 = []
# 종목.append(Samsung)
# 종목.append(Hyundea)
# 종목.append(LG)
#
# for x in 종목:
#     print(x.name, x.code, x.per)
# import random
#
# class Account:
#     deposit_number = 0
#     account_num = 0
#     def __init__(self, name, balance):
#         self.deposit_log = []
#         self.withdraw_log = []
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#         num1 = random.randint(0,999)
#         num2 = random.randint(0,99)
#         num3 = random.randint(0,999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + "-" + num2 + "-" + num3
#
#         Account.account_num = Account.account_num + 1
#     def deposit(self, money):
#         if money > 0:
#             self.balance += money
#             Account.deposit_number  += 1
#             if Account.deposit_number % 5 == 0:
#                 self.balance = int(self.balance * 1.01)
#                 print("이자 입금!")
#             print(f"{money}원을 입금하였습니다.{Account.deposit_number}회차")
#             print(f"잔액은 {self.balance}원 입니다.")
#
#     def withdraw(self, money):
#         if self.balance >= money:
#             self.balance -= money
#             print(f"{money}원을 인출하였습니다. \n잔액은 {self.balance}원 입니다.")
#         else:
#             print("잔액이 부족합니다.")
#
#     def display_info(self):
#         print(f"은행 이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account_number}")
#         print(f"잔고: {self.balance:,}")
#
#     def withdraw_history(self):
#         for amount in self.withdraw_log:
#             print(amount)
#
#     def deposit_history(self):
#         for amount in self.deposit_log:
#             print(amount)

# Minsu = Account("김민수", 100)
# print(Account.account_num)
# print()
# Minsu2 = Account("이민수", 100)
# print(Account.account_num)
# print()
# Minsu2.deposit(10000)
# print()
# Minsu2.withdraw(80)
# print()
# Minsu2.display_info()
# print()
# data = []
# k = Account("KIM", 10000000)
# b = Account("bea", 10000000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000)
#
# data.append(k)
# data.append(b)
# data.append(l)
# data.append(p)
#
# for x in data:
#     if x.balance >= 1000000:
#         x.display_info();print()
#
# k = Account("Kim", 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()
#
# k.withdraw(100)
# k.withdraw(200)
# k.withdraw_history()

# class 차():
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# car = 차(2,1000)
# print(car.바퀴)
# print(car.가격)
#
# class 자전차(차):
#     pass

