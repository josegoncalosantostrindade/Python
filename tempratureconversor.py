unit = input('Is this temperature in Celsius or Fahrenheit? (C or F): ')
temp = float(input('Enter the temperature: '))

if unit == 'C':
    temp = round((9 * temp) / 5 + 31, 1)
    print(f'The temperature in Fahrenheit is: {temp}ºF')
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f'The temperature in Celsius is: {temp}ºC')
else:
    print(f'{unit} is an invalid unit of measurement')