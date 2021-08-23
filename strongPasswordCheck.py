## Write a function that uses regular expression to make sure the password string is passed as strong
## Strong password has to be : at least 8 characters,contains both upper and lowercase
## and has at least one digit.

import re
import pyinputplus as pyip

def strongPasswordCheck(text):
    passwordRegex = re.compile(r'(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}')
    for i in passwordRegex.findall(text):
        return i

print('Hi and welcome to password check program')
while True:
    print('\nPlease enter password\nRemember your password has to include 2 uppercases, at least 1 digit, at least 1 special character,at least 3 lowercase characters and it has to be minimum 8 character long.')
    password = pyip.inputPassword(allowRegexes=[r'(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}'])
    if strongPasswordCheck(password):
        print('this is your password and it works: ' + password)
        break
    elif len(password)< 8:
        print('Your password has to be more than 8 characters ' + password)
    elif strongPasswordCheck(password) == None:
        print('Your password is not strong enough')