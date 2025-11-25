# txt
'''
file_path = 'readfiles/output.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to read taht file')
'''


# json
'''
import json
file_path = 'readfiles/output.json'

try:
    with open(file_path, 'r') as file:
        content = json.load(file)
        print(content)  # print(content['name'])
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to read taht file')
'''


# csv
import csv
file_path = 'readfiles/output.csv'

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line)  # print(line[0])
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to read taht file')