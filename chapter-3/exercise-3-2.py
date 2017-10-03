# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats

# Get length A from the user and convert it to a float
# Get width A from the user and convert it to a float
# Get length B from the user and convert it to a float
# Get width B from the user and convert it to a float

# Calculate area A

# Calculate area B

# Print each area, formatting the values to 2 decimal places

# if area A is greater, print "A is greater" message.

# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

Length_A = float(input('What is the length of rectangle A: '))
Length_B = float(input('What is the length of rectangle B: '))
Width_A = float(input('What is the width of rectangle A: '))
Width_B = float(input('What is the width of rectangle B: '))

Area_A = Length_A * Width_A
Area_B = Length_B * Width_B

print('The area of rectangle A is', format(Area_A, ".2f"))
print('The area of rectangle B is', format(Area_B, ".2f"))

if Area_A > Area_B:
    print('Rectangle A is greater')
elif Area_B > Area_A:
    print('Rectangle B is greater')
else:
    print('Rectangle A and rectangle B are equal')