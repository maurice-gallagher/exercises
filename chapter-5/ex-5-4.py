# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.

# define the main function

    # Define local float variables for loan, insurance, gas, oil, tires and maintenance

    # Get the amount of the monthly loan payment from the user.

    # Get the amount of the monthly insurance from the user.

    # Get the amount of the monthly gas from the user.

    # Get the amount of the monthly oil from the user.

    # Get the amount for monthly tire wear from the users.

    # Get the amount for monthly maintenance from the user.

    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.

# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.

    # Define local float variables for monthly total and annual total

    # calculate the monthly total
    
    # calculate the annual total

    # Print monthly and annual information, formatting float value to 2 decimal places.

# Call the main function to start the program

def main():
    mon_loan = float(input('What is your monthly loan payment: '))
    mon_insurance = float(input('What are your monthly insurance expences: '))
    mon_gas = float(input('What are your monthly gas expence: '))
    mon_oil = float(input('What are your monthly oil expence: '))
    mon_tire = float(input('What are your monthly tire expences:'))
    mon_maint = float(input('What are your monthly maintenance expences: '))
    
    expences(mon_gas, mon_insurance, mon_loan, mon_maint, mon_oil, mon_tire)

def expences(mon_gas, mon_insurance, mon_loan, mon_maint, mon_oil, mon_tire):
    mon_total = 0.0
    annual_total = 0.0
    
    mon_total = mon_gas + mon_insurance + mon_loan + mon_maint + mon_oil + mon_tire
    annual_total = mon_total * 12
    print('Monthly expences:', format(mon_total, ".2f"))
    print('Annual expences:', format(annual_total, ".2f"))
    
main()
    
    