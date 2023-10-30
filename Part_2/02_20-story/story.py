# Write your solution here
words = ''
last_word = ''

while True:

    user_input = input('Please type in a word: ')

    if user_input != 'end' and user_input != last_word:
        words += user_input + " "
        last_word = user_input
    else:
        break

print(words)
