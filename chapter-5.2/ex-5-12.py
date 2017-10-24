# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.

# define the main function

    # Define local variables to hold two integers

    # prompt the user for the first integer
    
    # prompt the user for the second integer

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments

 # Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.

	# if the first integer is greater, return the first integer

	# else, return the second integer

# Call the main function to start the program

def main():
    int1 = 0
    int2 = 0
    
    int1 = int(input('What is your first integer: '))
    int2 = int(input('What is your second integer: '))
    
    this_one = greater(int1, int2)
    print(this_one)
    
def greater(int1, int2):
    if int1 > int2:
        print('int one is larger than int two')
        return int1
    else:
        print('int two is larger than int one')
        return int2
main()
