from configparser import ConfigParser
from typing import List


class Settings:

    def __init__(self):
        file = 'config.ini'
        self.__config = ConfigParser(allow_no_value=True)
        dataset = self.__config.read(file)
        if len(dataset) == 0:
            self.loginPageURL = " "
            self.loginAssetURL = " "
            self.browserDriverPath = " "
            self.saveConfigFile()
        else:
            self.__readConfig()

    def __readConfig(self):
        print(self.__config['Settings'])
        self.loginPageURL = self.__config['Settings']['loginPageURL']
        self.loginAssetURL = self.__config['Settings']['loginAssetURL']
        self.browserDriverPath = self.__config['Settings']['browserDriverPath']

    def saveConfigFile(self):
        self.__config['Settings'] = {
            'loginPageURL': self.loginPageURL,
            'loginAssetURL': self.loginAssetURL,
            'browserDriverPath': self.browserDriverPath,
        }

        with open('config.ini', 'w') as configfile:
            self.__config.write(configfile)
