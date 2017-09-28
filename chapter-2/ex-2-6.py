# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats

# Constants for the state and county tax rates


# Get the amount of purchase from the user, casting it to a float.

# Calculate the state sales tax.

# Calculate the county sales tax.

# Sum the total tax.

# Calculate the total of the sale.

# Print detailed information about the sale, formatting all values to two decimal places.

amount = float(input('insert the cost of your item: '))

STATE_TAX = 6.12/100
COUNTY_TAX = 7/100

total_tax = STATE_TAX + COUNTY_TAX
total_price = total_tax + amount

print('your total price is', format(total_price, ".2f"))


