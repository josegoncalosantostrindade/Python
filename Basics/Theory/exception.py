try:
    number = int(input('Enter a number: '))
    print(1 / number)
except ZeroDivisionError:
    print('You can not divide by zero IDIOT!')
except ValueError:
    print('Enter only numbers please!')
finally:
    print('Do some cleanup here')