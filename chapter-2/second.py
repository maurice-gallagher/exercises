name = input("what is your name: ")
s_age = input('how old are you: ')
iage = float(s_age)

print('age is a',iage.__class__)
next_years_age = iage + 1
print(name, 'will be', next_years_age, 'years old next year at this time')
