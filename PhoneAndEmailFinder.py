import re, pyperclip

'''NumberAndEmail_Finder: finds a list of phone numbers and email addresses
 in a copied text found on the clipboard'''

#copy text from clipboard
board = str(pyperclip.paste())

#Displays the text on the clipboard
print(board, end='\n')

#to check for phone numbers
isPhoneNumber = re.compile(r'\(?\+?\d?\d?\d?\)?\s*\d{9,10}', re.I| re.DOTALL| re.VERBOSE)
#foundNumbers = isPhoneNumber.findall(board)
foundNumbers = []

#loop to get all numbers matching a phone number
for groups in isPhoneNumber.findall(board):
    foundNumbers.append(groups)

# to check for email addresses
isEmailAddress = re.compile(r'(\w+@\w+\.com?)|(\w+@ug.edu.gh)')
foundEmails = []

for groups in isEmailAddress.findall(board):
    foundEmails.append(groups[0])

"""Alternative line code:
#foundEmails = isEmailAddress.findall(board)"""

#display of found Phone Numbers
if len(foundNumbers) > 0:
    print('\nList of found phone Numbers:\n[', end='')
    print(",".join(foundNumbers), end='')
    print("]")
    
else:
    print('No phone numbers were found.')



#display of found Email Addresses
if len(foundEmails) > 0:
    print("\nList of found email Addresses:")
    print(foundEmails)
else:
    print('No Email Addresses were found.')

# results: Phone Numbers and Emails Addresses found are copied to back to the clipboard
pyperclip.copy('Phone Numbers:' + str(foundNumbers) + '\n' + 'Email Addresses:' + '\n' + str(foundEmails))

"""Examples of text I used to text my program:
#These are all numbers: 0502356786, +233502561025, 233 0956777777.
And these are emails: brainstormbright@gmail.com, stahiru008@ug.edu.gh
Rebecca phone number is 233 502611025 and her email is rebecca@gmail.com. 
Anuse phone number is 0243413822 and her email is anusebaby01@gmail.com
latifu@yahoomail.com and yahoo.com at sherif@      .com.I'm a Pythonista"""


