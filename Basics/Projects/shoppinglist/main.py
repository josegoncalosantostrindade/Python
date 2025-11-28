def get_file():
    # print('!!!In Get File!!!')

    global shopping_list
    shopping_list = []
    with open(file_path, 'r') as file:
        for line in file:
            shopping_list.append(line.strip())

    # print('!!!Out Get File!!!')

def main():
    global file_path
    file_path = '/Users/jgtrindade/Desktop/Curriculo/Python/Basics/Projects/shoppinglist/shop.txt'

    get_file()
    is_running = True
    temp_shopping_list = []

    while is_running:
        item_input = input('Enter an item for you shopping list (q to quit): ')

        if not item_input.lower().strip() == 'q':
            if not all(char.isalpha() for char in item_input.split()):
                # print('!!!In Verification Item!!!')

                print('Invalid item!')

                # print('!!!Out Verification Item!!!')
                continue
            else:
                item_input.capitalize()
                # print('!!!In Append To List!!!')

                temp_shopping_list.append(item_input)

                # print('!!!Out Append To List!!!')
                continue
        else:
            pass

        # print(temp_shopping_list)
        for item in temp_shopping_list:
            # print('!!!In Append To File!!!')

            if item in shopping_list:
                pass
            else:
                with open(file_path, 'a') as file:
                    file.write(f'{item}\n')

            # print('!!!Out Append To File!!!')

        get_file()
        is_running = False

    print('END')


if __name__ == '__main__':
    main()