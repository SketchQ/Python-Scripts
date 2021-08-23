#! python3
#phoneandemail.py - Finds phone numbers and email adresses on the clipboard

### This program will find the phone numbers and email adresses in a text and will paste it to the clipboard

##  -----  Broad Plan -----##
# 1 Get the text off the clipboard
# 2 Find all phone numbers and email adresses
# 3 Paste them onto the clipboard

## ------ How the code should work ----- ##
# 1. use the pyperclip module to copy and paste strings
# 2. Create two regexes, one for matching phone numbers and the other for matching email adresses
# 3. Find all matches, not just the first match, of both regexes
# 4. Neatly format the matched string into a single string to paste.
# 5. Display some kind of message if no matches were found in the text.

## Step 1: Create a regex for Phone numbers
import pyperclip,re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # Area code
    (\s|-|\.)?          # Seperator
    (\d{3})             # first 3 digits
    (\s|-|\.)           # Seperator
    (\d{4})             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
    )''',re.VERBOSE)

# Create email regex

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+       # Username
@                       #  @ Symbol
[a-zA-Z0-9.-]+          # domain name
(\.[a-zA-Z]{2,4})       # dot something    
)''',re.VERBOSE)

#  Find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


#  Copy Results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No phone numbers or email adresses found.")
