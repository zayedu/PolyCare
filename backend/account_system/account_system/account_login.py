from auth import Account
import openpyxl

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
    
    def find_login_credentials(loginID):
        '''
        Description: This method checks for login credentials in the
        Account Database.

        Args:
        loginID     (str)       User's loginID

        Requires: loginID

        Modifies: NA

        Returns: password OR NA
        '''
        page = Account.accdb.active
        '''Assuming that the first column(column A) is loginID. If not:
        for col in page.iter_cols(values_only = False):
            if col.value() == 'loginID' (the column that contains loginIDs)
            break'
        '''
        for row in page.iter_rows(values_only = True):
            if row[0] == loginID:               #username
                return row[1]                   #password
        else: 
            return 'loginID not found'
        
        


    


    
