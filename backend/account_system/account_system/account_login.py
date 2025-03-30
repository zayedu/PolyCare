from auth import Account
import csv

class AccountLogin(Account):

    def __init__(self, loginID: str, password: str):
        '''Description: Initializes 'Account' instance
        Args: 
        loginID     (str)       User's loginID
        password    (str)       User's password 

        Requires: loginID, password
        Modifies: NA
        Returns: NA      
        '''
        super().__init__(loginID, password)
    
    #not needed
    #def login_credentials_check(loginID):
        '''
        Description: This method checks for login credentials in the
        Account Database.

        Args:
        loginID     (str)       User's loginID

        Requires: loginID

        Modifies: NA

        Returns: password OR NA
        '''
      #  accdb = 'Data.csv'
       # with open (accdb, 'r') as accdb:
        #    row = ()
        


    


    
