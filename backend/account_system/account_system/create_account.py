from auth import Account
import csv
import bcrypt
from UserType import UserType 
'''
Potential change: The loginID and pw can only be set after successful 
verification from the govt. 
'''

class Create_Account(Account):
    '''Description: This class allows user to create an account and an
    'Account' instance.
    
    Args: 
    first_name:     (str)
    last_name:      (str)
    dateofbirth     (str)
    email           (str)
    govtid          (str)
    loginID         (str)
    password        (str)

    Requires: first_name, last_name, dateofbirth, email, govtid

    Modifies: loginID, password

    Returns: NA
    
    '''
    def __init__(self, first_name, last_name, dateofbirth, email, user_type_name: str, govtid, loginID = None, password = None):
        super().__init__(loginID)

        #all fields entered check
        if not all([first_name, last_name, dateofbirth, email, govtid]):
            raise ValueError("Missing input fields")
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.dateofbirth = str(dateofbirth).strip()
        self.email = email.lower().strip()  #making sure it is all lowercase
        self.govtid = str(govtid.strip()) #in case there are spaces
        self.user_type_name = user_type_name  #'Patient' or 'Physician' etc. -- front end display value1
        self.govtpath = "./backend/account_system/account_system/GovtIDs.csv"
        self.datapath = "./backend/account_system/account_system/Data.csv"
        self.Data_GovtCol = 2 #in govtids.csv

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email format")
        
        self._email = value.lower().strip()

        
    

    def govtid_verification(self):
        '''
        Description: verifies user input govtid with government records

        Requires: NA

        Returns: 
        status     (bool, str)     Verification status and messages
        '''

        try:
            with open (self.govtpath, 'r', newline='') as a:
                entry = csv.reader(a)
                next(entry)         #skips header
                for row in entry:
                    if (row[0].strip().title() == self.first_name and row[1].strip().title() == self.last_name and str(row[3].strip) == str(self.dateofbirth.strip())):
                        if row[2].strip() == self.govtid.strip():
                            return True, "Verification successful"
                        else:
                            return False, "ID does not match governement records"
                return False, "No matching government record found"

        except FileNotFoundError:
            return False, "Government database not found"
        except csv.Error:
            return False, "Error reading government records"
        except Exception as e:
            return False, "Unexpected error in govt verification: str{e}"

    def set_credentials(self, loginID, password):
        '''
        Description: sets loginID and password credentials
        
        Args: 
        loginID     (str)       User's loginID (to be set)
        password    (str)       User's password (to be set)

        Requires: loginID, password (user-entered)

        Returns: set loginID and password

        '''
        verified, msg = self.govtid_verification()
        if not verified:
            return msg
        
        self.loginID = loginID.strip()      #no spaces
        self.password = password
            #self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #more secure because salting
        return "Saved loginID and password"
    
    def check_account(self):
        '''
        Description: This method checks for the existence of an account in the Data.csv database
        by checking if the govtid entered by the user already exists in the database.
        
        Requires: NA

        Returns: 
            (bool,str)          True if account exists with a message 
        '''

        try:
            with open(self.datapath, 'r') as d:
                reader = csv.reader(d)
                next(reader)

                for row in reader:
                    if len(row) > self.Data_GovtCol:
                        if row[self.Data_GovtCol].strip() == self.govtid.strip():
                            return True, "Account already exists"
                        
                return False, f"New account will be created using: {self.loginID if hasattr(self, 'loginID') else 'New ID'}"
        
        except FileNotFoundError:
            return False, "Accounts database not found"
        except Exception as e:
            return False, f"Error checking account database: {str(e)}"

    def save_to_database(self):
        '''
        Description: Adds new user account to Data.csv

        Args: NA
        
        Requires: NA

        Returns: NA
        '''
        try: 
            if not hasattr(self, 'loginID') or not hasattr (self,'password'):
                #print("no loginID or pw")
                return False, "Account loginID and/or password not set"
            
            
            new_account, _ = self.check_account()
            if new_account:
                return False, "Account already exists"
            
            with open(self.datapath, 'a', newline='') as d: 

                writer = csv.writer(d)
                data_row = [self.loginID, 
                                 self.password, 
                                 self.email,
                                 UserType.get_value(self.user_type_name),                   #assuming any type of user and not the value is being selected at the front end
                                 self.govtid]
                print(data_row)
                writer.writerow(data_row)
            return True, "Account saved successfully"
        
        except Exception as e:
            return False, "Save failed" 
            


#tested by creating an account which was successful yay



if __name__ == '__main__':

    testuser = Create_Account('John', 'Smith', '06102014', 'hello@gmail.com', 'Patient', '56781230DD' )
    if testuser: 
        print("success")
    else:
        print("False")
        
    print(Create_Account.govtid_verification(testuser))

    print(Create_Account.check_account(testuser))

    print("setting loginID and pw:")
    print(Create_Account.set_credentials(testuser, 'test123', 'hello123'))
    print(Create_Account.save_to_database(testuser))




        
    
    

    