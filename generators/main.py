'''
def count_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

number = int(input('Enter a number to count to: '))

for n in count_to(number):
    print(n)
'''


def read_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()

file_path = 'generators/test.txt'
for line in read_file(file_path):
    print(line)