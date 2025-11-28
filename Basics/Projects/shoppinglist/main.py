file_path = 'Basics/Projects/shoppinglist/shop.txt'

'''try:
    with open(file_path, 'r') as file:
        content = file.read()
        # print(content)
except FileNotFoundError:
    print('File not found')'''

shopping_list = []
is_running = True

while is_running:
    item_input = input('Enter an item for you shopping list (q to quit): ').capitalize()

    if not item_input.lower().strip() == 'q':
        if not all(char.isalpha() for char in item_input.split()):
            print('!!!In Verification Item!!!')

            print('Invalid item!')

            print('!!!Out Verification Item!!!')
            continue
        else:
            print('!!!In Append To List!!!')

            shopping_list.append(item_input)

            print('!!!Out Append To List!!!')
            continue
    else:
        pass

    print(shopping_list)

    print('!!!In Append To File!!!')

    for item in shopping_list:
        print('!!!In Append To File!!!')

        with open(file_path, 'a') as file:
            file.write(f'{item}\n')

        print('!!!Out Append To File!!!')

print('END')