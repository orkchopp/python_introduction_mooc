# Write your solution here

password = input('Password: ')

while True:
    repeated_password = input('Repeat password: ')

    if password != repeated_password:
        print('They do not match!')
    else:
        print('User account created!')
        break