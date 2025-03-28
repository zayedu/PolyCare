from abc import ABC
#Openpyxl: used to access excel file 
from openpyxl import load_workbook
#import os


class Account(ABC):

    def __init__(self, loginID, password):
        self.loginID = loginID
        self.password = password
    #    self.dbfilepath = None
    #    self.accdb = load_workbook("Account Database.xlsx")
'''
 #double check error handling   
    def set_dbfilepath(self, dbfilepath):
        self.dbfilepath = dbfilepath
'''

if __name__ == '__main__':
    acc = Account('log1', 'pw')
    print(acc.loginID)
    print(acc.password)
