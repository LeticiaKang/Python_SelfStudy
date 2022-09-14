import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#class를 하나 생성
class Exam(QWidget):
    #QWdidget을 상속받아서 클래스를 생성한다
    def __init__(self):
        super().__init__()
        self.initUI() #함수(매서드)를 하나 만듦
    def initUI(self):
        btn = QPushButton("누르세요", self)
        btn.resize(btn.sizeHint()) #글씨를 기준으로 크기를 조절해주는
        btn.setToolTip("ToolTip입니다.  <b>안녕하세요<b/>")
        btn.move(20,30) #왼쪽에서 20, 위에서 30

        self.setGeometry(300,300,400,500)
        self.setWindowTitle("첫 번째 학습시간")
        self.show()

app = QApplication(sys.argv)
#모든 QT5 어플리케션은 객체를 생성해야 하는데 그걸 실행하는 코드
w = Exam()
sys.exit(app.exec_())