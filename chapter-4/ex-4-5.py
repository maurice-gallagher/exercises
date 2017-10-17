# Programming Exercise 4-5
#
# Program to compute total and average monthly rainfall over a span of years.
# This program gets a number of years from a user,
# then uses nested loops to prompt for rainfall for each month in each year
#	and calculate the total and the average monthly rainfall,
# then displays the number of months, total rainfall and average monthly rainfall

# Create float variables for total rainfall, monthly rainfall, average monthly rainfall

# Create int variables for number of years and number of months.

# Get number of years from the user

# Nested loop logic to loop through the years and their months
#
# Outer for loop for the number of years

	# Print the current year message

	# Inner loop for 12 months 

		# Get monthly rainfall for current month from the user
		
		# add monthly rainfall to total rainfall
		
		# increment number of months
		
# Calculate the average rainfall using total rainfall and number of months

# print the results on the screen, including details for total months, total rainfall,
#	and average monthly rainfall, formatting any floats to 2 decimal places.

total_rain = float
month_rain = float
avg_month_rain = float
years = int
months = int
total_rain = int

years = int(input('how many years: '))

for x in range(1, years +1):
	print('the year is', x)
	for i in range(1,13):
		month_rain = int(input('what is the rainfall for this month: '))
		total_rain =+ month_rain
		months = years * 12
avg_month_rain = (total_rain + months) / 12
print(months, 'months')
print(format(total_rain, ".2f"), 'total rain',) 
print(format(avg_month_rain, ".2f"), 'average monthly rain', )


