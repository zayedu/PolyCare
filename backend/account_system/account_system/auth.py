from abc import ABC
import bcrypt
import csv

#connect to front end for input id and password
#retest for clarity

class Account(ABC):

    def __init__(self, loginID):
        self.loginID = loginID
        self.accdbfilepath = 'Data.csv'
        self.storedhash = None
        

    def loginID_exists(self) -> bool:
        try:
            #can check file exists error that is not implemented
            with open (self.accdbfilepath, 'r') as file:
                entry = csv.reader("Data.csv")
                row = next(entry, None) #["loginID", "password"] #first row/header
                for row in file:
                    if row and row[0] == self.loginID:
                        self.storedhash = row[1]
                        return True
            return False 
            #create account pop up
            #call create account
        except Exception as e: 
            return False
        
    #input_passwprd - get pw that is entered by user
    def pw_verification(self, input_password) -> bool:
        if not self.storedhash:
            return False
        try: 
            return bcrypt.checkpw(
                input_password.encode("utf-8"),
                self.storedhash.encode("utf-8")
            )
        
        except Exception as e:
            print("Unexpected error verify password")

        #reset password connection

    




'''if __name__ == '__main__':
    acc = Account('log1', 'pw')
    print(acc.loginID)
    print(acc.password)
'''