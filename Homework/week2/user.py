from bank_account import Bank
import random
import json

def createUser():
    # while username:
    # try:
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    account_number = random.randrange(1000000, 9999999)
    user = Bank(username, password, account_number)
    if len(username) <= 15:
        print(username, password, account_number)
        with open('bankFile.json', 'wt') as bankFile:
            data = json.loads(bankFile)
            data['bank_details'].append(bank_data)
            json.dump(bank_data, bankFile, indent = 4)
    #     elif len(username) > 15:
    #         raise Exception
    # except Exception:
    #     print('Please enter a username less than 15 characters')
    # else:
    #     bankFile.close()



createUser()
