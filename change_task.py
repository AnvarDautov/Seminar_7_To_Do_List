import csv
import datetime
import logger


def change_task():

    print('СПИСОК ТЕКУЩИХ ЗАДАЧ:')

    with open('list_of_current_tasks.csv', 'r', encoding='utf-8') as file:
        task_list = csv.reader(file, delimiter='\t')
        current_task_list = []
        counter = 1
        for line in task_list:
            print(counter, line[-1], sep=' ')
            current_task_list.append(line)
            counter += 1

    task_to_be_changed = input('Введите номер задачи, что вы хотели бы изменить: ')

    if task_to_be_changed.isdigit() and 0 < int(task_to_be_changed) <= len(current_task_list):
        prev_task = current_task_list[int(task_to_be_changed) - 1].copy()

        new_name = input('ВВЕДИТЕ НОВОЕ ИМЯ ЗАДАЧИ:')
        current_task_list[int(task_to_be_changed) - 1][-1] = new_name

        print(f'ЗАДАЧА <{prev_task[-1]}> БЫЛА ИЗМЕНЕНА НА <{new_name}>')

        with open('list_of_current_tasks.csv', 'w', newline='', encoding='utf-8') as file:
            task = csv.writer(file, delimiter='\t')
            for elem in current_task_list:
                task.writerow(elem)

    else:
        print('Введено некорректное значение')
