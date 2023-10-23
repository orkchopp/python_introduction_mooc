# Write your solution here
fahreinheit = int(input('Please type in a temperature (F):'))
celcius = (fahreinheit - 32) * 5/9

if celcius < 0:
    print(f'{fahreinheit} degrees Fahrenheit equals {celcius} degrees Celsius')
    print("Brr! It's cold in here!")
else:
    print(f'{fahreinheit} degrees Fahrenheit equals {celcius} degrees Celsius')