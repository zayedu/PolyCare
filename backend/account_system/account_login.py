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
        super().__init__(loginID)
        self.datapath = "account_system/account_system/Data.csv"
        self.password = password

    def login(self) -> bool:
        '''
        Description: allows user to login
        Args:
        self.loginID        (str)       User entered loginID
        self.password       (str)       User entered password

        Requires: login_ID, password
        Modifies: NA
        Returns: Message    (str) 
        '''
        
        user_input_acc = self.find_account()
        if not user_input_acc: 
            raise Exception("Account not found")
        
        if user_input_acc["password"] == self.password:
            print('logged in')
            return "Successfully logged in"
        else:
            return "Login failed. Reset credentials or contact app support."
        
    def find_account(self) -> dict:
        '''
        Description: Finds user account row in database
        Args:
        self.datapath       (str)       Path to accounts database

        Requries: loginID, password
        Modifies: NA
        Returns: 
        row                 (dict)      Row with user info from Account database

        '''
        try:
            with open(self.datapath, 'r', newline='') as f:
                for row in csv.DictReader(f):
                    if row["loginID"] == self.loginID:
                        return row
        except FileNotFoundError:
            pass
        return None

    
if __name__ == '__main__':
    user = AccountLogin('Sfwre12', '3rdYear!')
    print(user.login())
        


    


    
