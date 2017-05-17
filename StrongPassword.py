import re

low_case_check = re.compile(r'[a-z]')
up_case_check = re.compile(r'[A-Z]')
is_dig_check = re.compile(r'[0-9]')

while True:
    password = input("Enter your password or leave blank for exit: ")
    if password == "":
        break
    if (low_case_check.search(password) and up_case_check.search(password))and (is_dig_check.search(password) and len(password)>8):
           print('Strong password')
    else:
        print('Bad password')
