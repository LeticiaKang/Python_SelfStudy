import sys
from PyQt5.QtWidgets import *

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar() #상태표시줄
        self.statusBar().showMessage("상태표시줄") #상태표시줄 객체를 받아옴

        menu = self.menuBar()  #메뉴바 생성하기
        menu_file = menu.addMenu("File") # 그룹 생성하기(이름 붙여서)
        menu_edit = menu.addMenu("Edit")

        file_exit = QAction("Exit", self) #메뉴 그룹 안에 객체 생성
        file_exit.setShortcut("Ctrl + Q")
        file_exit.setStatusTip("누르면 영원이 안녕") #상태표시줄에 설명 표시

        menu_file.addAction(file_exit)  #매뉴 등록
        self.resize(450,400)
        self.show()

app = QApplication(sys.argv)
W = Exam()
sys.exit(app.exec_())