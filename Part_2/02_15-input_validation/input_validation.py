from math import sqrt
# Write your solution here

while True:
    user_input = int(input('Please type in a number: '))

    if user_input > 0:
        print(sqrt(user_input))
    elif user_input < 0:
        print('Invalid number')
    else:
        break

print('Exiting...')