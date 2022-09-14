# 창 띄우기

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *  # 아이콘 만들기
from PyQt5.QtCore import QCoreApplication   # 창닫기

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn_percent = QPushButton('%', self)
        btn_percent.move(0, 250)
        btn_percent.resize(125,75)

        btn_ce = QPushButton('CE', self)
        btn_ce.move(125, 250)
        btn_ce.resize(125,75)

        btn_c = QPushButton('C', self)
        btn_c.move(250, 250)
        btn_c.resize(125,75)

        btn_x = QPushButton("지우기", self)
        btn_x.move(375, 250)
        btn_x.resize(125,75)

        btn_fraction = QPushButton('1/x', self)
        btn_fraction.move(0, 325)
        btn_fraction.resize(125,75)

        btn_quare = QPushButton('x²', self)
        btn_quare.move(125, 325)
        btn_quare.resize(125, 75)

        btn_root = QPushButton('√', self)
        btn_root.move(250, 325)
        btn_root.resize(125, 75)

        btn_did = QPushButton('÷', self)
        btn_did.move(375, 325)
        btn_did.resize(125, 75)

        btn_seven = QPushButton('7', self)
        btn_seven.move(0, 400)
        btn_seven.resize(125, 75)

        btn_eghit = QPushButton('8', self)
        btn_eghit.move(125, 400)
        btn_eghit.resize(125, 75)

        btn_nine = QPushButton('9', self)
        btn_nine.move(250, 400)
        btn_nine.resize(125, 75)

        btn_multi = QPushButton('×', self)
        btn_multi.move(375, 400)
        btn_multi.resize(125, 75)

        btn_four = QPushButton('4', self)
        btn_four.move(0, 475)
        btn_four.resize(125, 75)

        btn_five = QPushButton('5', self)
        btn_five.move(125, 475)
        btn_five.resize(125, 75)

        btn_six = QPushButton('6', self)
        btn_six.move(250, 475)
        btn_six.resize(125, 75)

        btn_minus = QPushButton('-', self)
        btn_minus.move(375, 475)
        btn_minus.resize(125, 75)

        btn_one = QPushButton('1', self)
        btn_one.move(0, 550)
        btn_one.resize(125, 75)

        btn_two = QPushButton('2', self)
        btn_two.move(125, 550)
        btn_two.resize(125, 75)

        btn_three = QPushButton('3', self)
        btn_three.move(250, 550)
        btn_three.resize(125, 75)

        btn_plus = QPushButton('+', self)
        btn_plus.move(375, 550)
        btn_plus.resize(125, 75)

        btn_pm = QPushButton("±", self)
        btn_pm.move(0, 620)
        btn_pm.resize(125, 75)

        btn_zero = QPushButton('0', self)
        btn_zero.move(125, 620)
        btn_zero.resize(125, 75)

        btn_period = QPushButton('.', self)
        btn_period.move(250, 620)
        btn_period.resize(125, 75)

        btn_equal = QPushButton('=', self)
        btn_equal.move(375, 620)
        btn_equal.resize(125, 75)


        btn = QPushButton("닫기", self)
        btn.move(400, 0)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(0, 100)
        self.line_edit.resize(500, 100)

        # self.statusbar = QStatusBar(self)
        # self.setStatusBar(self.statusbar)
        # self.statusBar.showMessage('만드는 중....')

        self.setWindowTitle('계산기')      # setWindowTitle : 창의 이름을 설정
        self.setWindowIcon(QIcon("C:/Users/USER/Desktop/calculator.png"))     # setWindowIcon(QIcon("아이콘이름.png")): 아이콘을 창 이름 옆에 넣어줌
        # 아이콘을 다른 경로에 저장해 두었다면 경로까지 입력해야 함.
        self.move(300, 300)    # move : 화면에 위치하는 곳을 조정
        self.resize(500, 710)     # resize : 창의 크키를 조정
        self.show()         # show : 화면에 나타나게 함


if __name__ == '__main__':      # 모르겠음
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

