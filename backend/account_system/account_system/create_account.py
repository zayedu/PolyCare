from auth import Account
import csv
import bcrypt
'''
Potential change: The loginID and pw can only be set after successful 
verification from the govt. 
'''

class Create_Account(Account):
    def __init__(self, first_name, last_name,
                 dateofbirth, email, govtid, loginID = None, password = None):
        super().__init__(loginID, password)
        self.first_name = first_name
        self.last_name = last_name
        self.dateofbirth = dateofbirth
        self.email = email
        self.govtid = govtid
        self.govtpath = "GovtIDs.csv"
        #check if all fields are entered
    

    def govtid_verification(self):
        try:
            with open (govtpath, 'r') as a:
                entry = csv.reader()
                next(entry, None)
                for row in entry: 
                    if row[0] == self.first_name and row[1] == self.last_name and row[3] == self.dateofbirth:
                        if row[2] == self.govtid:
                            print("Verification successful")
                        else:
                            print("unable to verify")
                    else:
                        pass

        except FileNotFoundError:
            return False, "Govt db not found"
        except csv.Error:
            return False, "csv incompatible"
        except PermissionError:
            return False, "Access denied"
        except Exception as e:
            return False, "Unexpected error in govt verification"
        

'''
if __name__ == '__main__'
with open ("GovtIDs.cs")'''