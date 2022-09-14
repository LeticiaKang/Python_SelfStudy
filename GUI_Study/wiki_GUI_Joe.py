import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# QtWidgets에는 QApplication과 QWidget이 들어있음

# app = QApplication(sys.argv)
#
# button = QPushButton("Button")
# button.show()
#
# label = QLabel("Label")
# label.show()
#
# app.exec_()

class MyWindow(QMainWindow):
    #PyQt가 제공하는 QMainWindow를 상속받아 MyWindow라는 클래스를 정의

    def __init__(self):
        super().__init__()
    # MyWindow(자식클래스)에서 __init__()매서드를 정의함으로
    # QMainWindow(부모클래스)의 __init__()은 더 이상 호출되지 않는다.
        self.serGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon("-_-zz.png"))

app = QApplication(sys.argv)
    # sys모듈에 있는 argv라는 변수
window = MyWindow()
window.show()
app.exec_()
