import re, pyperclip

'''NumberAndEmail_Finder: finds a list of phone numbers and email addresses
 in a copied text found on the clipboard'''

#copy text from clipboard
board = str(pyperclip.paste())

#Displays the text on the clipboard
print(board, end='\n\n')

#to check for phone numbers
isPhoneNumber = re.compile(r'\(?\+?\d?\d?\d?\)?\s*\d{9,10}', re.I| re.DOTALL| re.VERBOSE)
foundNumbers = isPhoneNumber.findall(board)

# to check for email addresses
isEmailAddress = re.compile(r'(\w+@\w+\.com?)|(\w+@ug.edu.gh)')
foundEmails = isEmailAddress.findall(board)

#display of found Phone Numbers
if len(foundNumbers) > 0:
    print('list of found phone Numbers:')
    for i in range(len(foundNumbers)):
        print(foundNumbers[i], end='  ')
else:
    print('No phone numbers were found.')

#display of found Email Addresses
foundEmails = list(foundEmails)
if len(foundEmails) > 0:
    print('\nlist of found Email Addresses:')
    for i in range(len(foundEmails)):
        print(foundEmails[i], end='  ')
else:
    print('No Email Addresses were found.')

# results: Phone Numbers and Emails Addresses found are copied to back to the clipboard
pyperclip.copy('Phone Numbers:' + str(foundNumbers) + '\n' + 'Email Addresses:' + '\n' + str(foundEmails))

"""Example of text I used to test my program:
#These are all numbers: 0502356786, +233502561025, 233 0956777777.
And these are emails: brainstormbright@gmail.com, stahiru008@ug.edu.gh
Rebecca phone number is 233 502611025 and her email is rebecca@gmail.com. 
Anuse phone number is 0243413822 and her email is anusebaby01@gmail.com"""


