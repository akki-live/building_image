import random

print("Welcome to Password Generator")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()><?:;'

number = input('Amount of password to generate: ')
number = int(number)

lenght = input('Your password lenght: ')
lenght = int(lenght)

print('here are you passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)