from UserType import UserType
from auth import Account
import csv

def main():
    filepath = './backend/account_system/account_system/Data.csv'
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['boo456', '23ug', 'he@gmail.com', '3', 'hsudf'])

if __name__ == '__main__':
    main()
