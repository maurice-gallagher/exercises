# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.


# Global constants for minimum, maximum and mass multiplier values


# Variables for weight and mass initialized as floats   


# Get mass from user and convert it to a float


# Calculate weight using the mass multiplier constant


# Display the weight

# If weight > maximum or < than minimum display an appropriate message

mass = float(input('Enter a mass in kg to be converted to Newtons: '))
MIN = 9.81 
MAX = 1000
newtons = float(mass*9.81)

if newtons > MAX or newtons < MIN:
    print('This is not okay')

else:
    print(format(newtons, ".2f"), 'Newtons')
