# Write your solution here
year = int(input('Please type in a year: '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('This year is a leap year.')
else:
    print('This year is not a leap year.')