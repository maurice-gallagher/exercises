# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.
number = int(input('Give a number from 1-10 to get a Roman numeral: '))
# Get number from user and convert it to an int

# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.
if number == 1:
    print('I')
if number == 2:
    print('II')
if number == 3:
    print('III')
if number == 4:
    print('IV')
if number == 5:
    print('V')
if number == 6:
    print('VI')
if number == 7:
    print('VII')
if number == 8:
    print('VIII')
if number == 9:
    print('IX')
if number == 10:
    print('X')
elif number > 10:
    print('This number is too high')
elif number < 1:
    print('This number is too low')
        
# use a final else to display an error if number is out of range.

# display the numeral on the screen.






