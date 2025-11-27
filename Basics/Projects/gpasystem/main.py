def generate_report(user, grades, max, min, media):
    print('!!!In generateReport!!!')

    print('\n***** REPORT *****')
    print('******************')
    print(f'Student: {user}')

    print('\n***** GRADES *****')
    for key, value in grades.items():
        print(f'{key}: {value}')
    print('******************')

    print(f'Highest grade: {list(max.values())[0]}') # if there's only one value in the list
    print(f'Lowest grade: {list(min.values())[0]}') # if there's only one value in the list
    print(f'Media: {media}')
    print('******************')

    print('!!!Out generateReport!!!')
def get_max_grade(grades):
    # print('!!!In max!!!')

    maxKey = max(grades, key=grades.get)
    maxValue = max(grades.values())

    # print('!!!Out max!!!')
    return {maxKey: maxValue}


def get_min_grade(grades):
    # print('!!!In min!!!')

    minKey = min(grades, key=grades.get)
    minValue = min(grades.values())

    # print('!!!Out min!!!')
    return {minKey: minValue}


def get_media(grades):
    # print('!!!In media!!!')

    media = 0
    for value in grades.values():
        media += int(value)

    media /= len(grades)
    
    # print('!!!Out media!!!')
    return media

    
def main():
    grades = {}
    is_running = True

    while is_running:
        user = input('Enter your name: ').capitalize()
        user_is_valid = all(char.isalpha() for char in user.split())
        if not user_is_valid:
            print('Invalid name!')
            continue
        
        while is_running:
            discipline = input('Enter the name of the discipline: ')
            gradeDiscipline = input('Enter the grade: ')

            grades.update({discipline: gradeDiscipline})
            
            print('\n******************')
            choice = input('Would you like to add more disciplines and his grades? (y/n): ').lower()
            if choice == 'n':
                is_running = False
            else:
                continue

            max_grade = get_max_grade(grades)
            min_grade = get_min_grade(grades)
            media_grades = get_media(grades)

            generate_report(user, grades, max_grade, min_grade, media_grades)

if __name__ == '__main__':
    main()