# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values


# Get the amount of projected sales.
# be sure to convert the input to a float


# Calculate the projected profit using a 23% profit margin.


# Print the projected profit.
# be sure to format the output to two decimal places

sales = input('What are your sales: ')
profit = float(sales)
projected_profit = profit * .23

print('your profit is', '%.2f' % projected_profit)