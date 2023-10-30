# Write your solution here
gift_val = int(input('Value of gift: '))

if gift_val < 5000:
    print("No tax!")
elif 5000 <= gift_val <= 25000:
    print(f'Amount of tax: {100 + (gift_val - 5000) * 0.08} euros')
elif 25000 <= gift_val <= 55000:
    print(f'Amount of tax: {1700 + (gift_val - 25000) * 0.1} euros')
elif 55000 <= gift_val <= 200000:
    print(f'Amount of tax: {4700 + (gift_val - 55000) * 0.12} euros')
elif 200000 <= gift_val <= 1000000:
    print(f'Amount of tax: {22100 + (gift_val - 200000) * 0.15} euros')
else:
    print(f'Amount of tax: {142100 + (gift_val - 1000000) * 0.17} euros')