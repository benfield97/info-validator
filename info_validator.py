import pyinputplus as pyip
import datetime
import re


while True:

    name = pyip.inputStr("What is your name? ")

    if all(x.isalpha() or x.isspace() for x in name):

        name = name.split()

        if len(name) < 2:
            print("Please enter both a first and last name")
            continue
        else:
            break

    else:
        print("Name Invalid: Please only use letters")
        continue


birthday = pyip.inputDate(prompt="Please enter your date of birth (example: 4 Jan 2001) ", formats=['%d %b %Y'])

# will need to check address with a regex expression

while True:

    pattern = re.compile(r'\d+\s[A-z]+\s[A-z]+,\s(VIC|NSW|TAS|ACT|NT|SA|WA)', re.IGNORECASE)

    address = input('Enter you address (Example: 4 Example St, VIC) ')

    result = pattern.search(address)

    if result:
        break
    else:
        print('Address Invalid')


# check that address is
