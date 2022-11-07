import configparser
from time import strftime
import os

# ConfigParser 클래스
from attr import _config


class ConfigClass:
    _file_path = ""
    _is_exist = True
    _config = None

    def __init__(self):
        # 1. config 객체 생성
        _config = configparser.ConfigParser()

        # 2. ini파일 경로 가져오기
        _is_exist = self.GetFilePath()

    def GetFilePath(self):
        _file_path = os.getcwd() + "\config.ini"
        if os.path.isfile('config.ini') == True:
            print("파일이 있습니다.", _file_path)
            _config.read('config.ini', encoding='utf-8')
        else:
            print("파일이 없습니다.", _file_path)

    def SaverConfig(self, section, key):
        with open(_file_path, 'w', encoding='utf-8') as configfile:
            _config.write(configfile)