from auth import Account
import csv


class delete_account(Account):
    def __init__(self, loginID):
        super().__init__(loginID)
        self.datapath = "./backend/account_system/account_system/Data.csv"
    
    def remove_from_db(self):
        headers = ''
        with open(self.datapath, 'r', newline='') as old:
            updated_list = []
            reader = csv.reader(old)
            headers = next(reader)
            col_index = headers.index('loginID')
            for row in reader:
                if row[col_index] != self.loginID:
                    updated_list.append(row)

        with open(self.datapath, 'w', newline='') as new:
            writer = csv.writer(new)
            writer.writerow(headers)
            writer.writerows(updated_list)



            



 
    


    def col_number(self):
        with open(self.datapath, 'r', newline='') as f:
            reader = csv.reader(f)
            first_row = next(reader)
            try:
                return first_row.index('loginID')
            except ValueError:
                return 'unable to find column'
   
if __name__ == '__main__':
    tbd = delete_account('boo456')

    x = tbd.remove_from_db()
   # print(x)








'''
    def verify_creds_deletion(loginID, password):
        try:
            with open(self.dbpath, 'r') as f: 
                reader = csv.reader(f)
                for row in reader:
                    if row['loginID'] == loginID:
                        if bcrypt.checkpw(password.encode(), row['password'].encode()):
                            return True
'''                        



