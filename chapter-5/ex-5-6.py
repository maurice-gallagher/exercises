# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.

# Global constants for fat calories per gram and carb calories per gram

# define the main function

    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    
    # Get grams of fat from the user.

    # Get grams of carbs from the user.

    # Calculate calories from fat.

    # Calculate calories from carbs.

    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments

# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.

	# print each piece of information with floats formatted to 2 decimal places.

# Call the main function to start the program

FAT_CAL_PER_GRAM = 9
CARB_CAL_PER_GRAM = 4

def main():
    grams_fat = 0.0
    grams_carbs = 0.0
    cals_fat = 0.0
    cals_carbs = 0.0
    
    grams_fat = float(input('How many grams of fat: '))
    grams_carbs = float(input('How many grams of carbs: '))
    cals_fat = grams_fat * FAT_CAL_PER_GRAM
    cals_carbs = grams_carbs * CARB_CAL_PER_GRAM
    
    calorie_details(grams_carbs, grams_fat, cals_carbs, cals_fat)
        
def calorie_details(grams_carbs, grams_fat, cals_carbs, cals_fat):
    print('Grams of fat:', format(grams_fat, ".2f"))
    print('Grams of carbs', format(grams_carbs, ".2f"))
    print('Calories from fat', format(cals_fat, ".2f"))
    print('Calories from carbs', format(cals_carbs, ".2f"))
    
main()


