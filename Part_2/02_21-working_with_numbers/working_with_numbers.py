# Write your solution here
count = 0
sumn = 0
positive = 0
negative = 0

print('Please type in integer numbers. Type in 0 to finish.')

while True:
    number = int(input('Number: '))

    if number == 0:
        break
    
    count += 1
    print(f'Numbers typed in {count}')

    sumn += number
    print(f'The sum of the numbers is {sumn}')

    print(f'The mean of the numbers is {sumn / count}')

    if number < 0:
        negative += 1
    else:
        positive += 1
    print(f'Positive numbers {positive}')
    print(f'Negative numbers {negative}')
