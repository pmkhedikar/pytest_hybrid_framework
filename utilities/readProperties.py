import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\config\\config.ini")

class ReadConfig():

    @staticmethod
    def getAppUrl():
        url = config.get("commonInfo","baseURL")
        return url

    @staticmethod
    def getUserEmail():
        userEmail = config.get("commonInfo", "email")
        return userEmail

    @staticmethod
    def getPassword():
        password = config.get("commonInfo", "password")
        return password

