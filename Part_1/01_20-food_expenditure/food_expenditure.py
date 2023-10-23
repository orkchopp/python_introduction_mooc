# Write your solution here
eat_out = int(input('How many times a week do you eat at the student cafeteria?'))
price_of_lunch = float(input('The price of a typical student lunch?'))
price_of_groceries = float(input('How much money do you spend on groceries in a week?'))


weekly_caf_spending = eat_out * price_of_lunch
daily_spending = (weekly_caf_spending + price_of_groceries) / 7
weekly_spending = weekly_caf_spending + price_of_groceries
print('Average food expenditure:')
print(f'Daily: {daily_spending} euros')
print(f'Weekly: {weekly_spending} euros')