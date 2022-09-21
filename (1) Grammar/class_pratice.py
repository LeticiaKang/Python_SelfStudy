class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4,2)
print("a.add()값 :", a.add())


#다른 파일에서 정의된 함수 사용(모듈)
import Module_1
print("5 + 6 =",Module_1.add(5,6))

from Module_1 import divide
print("12 ÷ 4 = ", divide(12, 4))

import Module_1





