import json
file_path = '/Users/jgtrindade/Desktop/Curriculo/Python/Basics/Projects/tasksystem/tasks.json'

class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.is_completed = False

class TaskManager(Task):
    def completed_task(self):
        self.is_completed = True
        print(f'Task "{self.title}" is completed!')

def remove_task(title):
    with open(file_path, 'r') as file:
        tasks = json.load(file)

    tasks = [task for task in tasks if task.get('title') != title]

    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)  

def add_task(title, description, priority):
    task = Task(title, description, priority)
    
    try:
        with open(file=file_path, mode='r') as file:
            tasks = json.load(file)
    except FileExistsError:
            print('That file already exists!')

    tasks.append(task.__dict__)
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)  
    print('Task added with success')
    list_priority()

def complete_task(title):
    with open(file_path, 'r') as file:
        tasks = json.load(file)

    for task in tasks:
        if task.get('title') == title:
            task['is_completed'] = True
            print(f'Task "{title}" is completed!')

    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def list_priority():
    with open(file_path, 'r') as file:
        tasks = json.load(file)

    tasks_sorted = sorted(tasks, key=lambda x: int(x['priority']))

    with open(file_path, 'w') as file:
        json.dump(tasks_sorted, file, indent=4)

def menu():
    try:
        with open(file_path, 'r') as file:
            content = json.load(file)
            # print(content)
    except FileNotFoundError:
        print('That file was not found')
    except PermissionError:
        print('You do not have permission to read taht file')
    except json.JSONDecodeError:
        print('File is empty!')
        content = []

    print('\n************************')
    print('***** TASK MANAGER *****')
    print('************************')

    # Print every task in file
    print('\n************************')
    for line in content:
        print(f'{line['title']}: {line['description']} - {line['priority']}')
    print('************************\n')

    print('Option 1: ADD TASK')
    print('Option 2: REMOVE TASK')
    print('Option 3: COMPLETE TASK')
    print('Option 4: QUIT')

    def action(option):
        match option:
            case '1':
                title = input('Task title: ')
                description = input('Task description: ')
                priority = input('Task priority (1-5): ')
                add_task(title, description, priority)
            case '2':
                title = input('Task title: ')
                remove_task(title)
            case '3':
                title = input('Task title: ')
                complete_task(title)
            case '4':
                return
            case _:
                print('Invalid choice!')

    choice = input('Option: ')
    action(choice)

def main():
    is_running = True
    
    while is_running:
        menu()

        is_running = False

        # task = Task('Teste', 'Teste para classes', 4)
        # print(task.title)
        # print(task.description)
        # print(task.priority)

        '''title = input('Task title: ')
        description = input('Task description: ')
        priority = input('Task priority (1-5): ')
        task = Task(title, description, priority)

        print(task.title)
        print(task.description)
        print(task.priority)

        try:
            with open(file=file_path, mode='a') as file:
                json.dump(task.__dict__, file, indent = 4)
                print(f'json file "{file_path}" was created')
        except FileExistsError:
            print('That file already exists!')'''



if __name__ == '__main__':
    main()