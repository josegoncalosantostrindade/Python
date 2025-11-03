'''
# name = input('Enter your full name: ')
phone_number = input('Enter your phone #: ')

# result = len(name)
# result = name.find('G')
# result = name.rfind('u')
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count('-')
# phone_number = phone_number.replace('-', ' ')

print(phone_number)
print(help(str))
'''

# Exercise: Validate user input
username = input('Enter a username: ')

if len(username) > 12:
    print('Your username can not be more than 12 characters')
elif not username.find(' ') == -1:
    print('Your username can not contain spaces')
elif not username.isalpha():
    print('Your username can not contain numbers')
else:
    print(f'Welcome {username}')