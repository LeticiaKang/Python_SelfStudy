# pyi-makespec --noconsole --onefile QT.py
# pyinstaller QT.spec
# 실행파일 만들기 : Python 파일이 있는 폴더로 이동한 다음, 아래 명령어를 입력하면 해당 폴더에 실행파일이 만들어집니다.
# pyinstaller QT.py
# 콘솔창 없이 실행파일 하나만
# pyinstaller -w -F QT.py
# pyinstaller -w --onefile QT.py
# 수정된 스팩파일 빌드 pyinstaller QT.spec

#1) 라이브러리 import
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os

from ConfigManager import ConfigClass
from NaverCrawling import news_crawling,login

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#2) UI 파일 연결 -> 같은 경로에 위치
form = resource_path("NaverCrawling.ui")
form_class = uic.loadUiType(form)[0]


#3) 화면을 띄우는 클래스 선언
class WindowClass(QMainWindow, form_class) :

    _config = ConfigClass()

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self._config = ConfigClass()

    # 버튼 이벤트
        self.PushButtonLogin.clicked.connect(self.ButtonEventLogin)
        self.PushButtonSite.clicked.connect(self.ButtonEventSite)

    def loadConfig(self):
        try:
            config_site = self._config.GetConfigData(self._config.section_main, self._config.key_site)
            config_id = self._config.GetConfigData(self._config.section_main, self._config.key_id)
            config_pw = self._config.GetConfigData(self._config.section_main, self._config.key_pw)

            self.lineEdit_SITE.setText(config_site)
            self.lineEdit_ID.setText(config_id)
            self.lineEdit_PWD.setText(config_pw)

            print(config_site, config_id, config_pw)
        except Exception as e:
            print(e)

    # btn_1이 눌리면 작동할 함수
    def ButtonEventLogin(self):
        print("로그인 버튼을 클릭했습니다.")
        print(self.lineEdit_ID.text())  # Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineEdit_PWD.text())
        login(self.lineEdit_ID.text(), self.lineEdit_PWD.text())

        try:
            # site = self.lineEdit_SITE.text()
            id_text = self.lineEdit_ID.text()
            pw = self.lineEdit_PWD.text()
            msg_info = "id = {0},  pw = {1}".format(id_text, pw)
            QMessageBox.about(self, "message", msg_info)

            # self._config.SaveConfig(self._config.section_main, self._config.key_site, site)
            self._config.SaveConfig(self._config.section_main, self._config.key_id, id_text)
            self._config.SaveConfig(self._config.section_main, self._config.key_pw, pw)

            self._config.WriteConfig()
        except Exception as e:
            print(e)

    # btn_2가 눌리면 작동할 함수
    def ButtonEventSite(self):
        print('사이트를 입력했습니다.')
        print(self.lineEdit_SITE.text())
        try:
            site = self.lineEdit_SITE.text()

            msg_info = "site = {0}".format(site)
            QMessageBox.about(self, "message", msg_info)

            self._config.SaveConfig(self._config.section_main, self._config.key_site, site)

            self._config.WriteConfig()
        except Exception as e:
            print(e)

        url_list, title_list = news_crawling(self.lineEdit_SITE.text())
        print(url_list)
        crawl_cnt = len(url_list)
        for i in range(crawl_cnt):
            self.TableWidgetCrawling.setItem(i, 0, QTableWidgetItem(title_list[i]))
            self.TableWidgetCrawling.setItem(i, 1, QTableWidgetItem(url_list[i]))
            print("완료~")


# 4) 위에서 선언한 클래스를 실행 : QMainWindow 부모 클래스의 show 함수 실행
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