# pyinstaller -w -F NaverCrawlingUI.py
# pyinstaller NaverCrawlingUI.py

#1) 라이브러리 import
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#2) UI 파일 연결 -> 같은 경로에 위치
form = resource_path("NaverCrawling.ui")
form_class = uic.loadUiType(form)[0]


#3) 화면을 띄우는 클래스 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    #버튼에 기능을 연결하는 코드
        self.btn1.clicked.connect(self.button1Function)
        self.btn2.clicked.connect(self.button2Function)

    # TextEdit과 관련된 버튼에 기능 연결
        self.inputID_2.toPlainText()
        self.inputPWD.toPlainText()

#btn_1이 눌리면 작동할 함수
    def button1Function(self) :
        print("btn1 Clicked")
#btn_2가 눌리면 작동할 함수
    def button2Function(self) :
        print("btn2 Clicked")
        print(self.inputID_2.toPlainText())
        print(self.inputPWD.toPlainText())



#4) 위에서 선언한 클래스를 실행 : QMainWindow 부모 클래스의 show 함수 실행
if __name__ == '__main__':
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    # QtWidgets모듈에 QApplication클래스가 정의되어 있음
    app.exec_()