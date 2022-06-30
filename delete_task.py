import csv
import datetime
import logger


def delete_task():

    print('СПИСОК ТЕКУЩИХ ЗАДАЧ:')

    with open('list_of_current_tasks.csv', 'r', encoding='utf-8') as file:
        task_list = csv.reader(file, delimiter='\t')
        current_task_list = []
        counter = 1

        for line in task_list:
            print(counter, line[-1], sep=' ')
            current_task_list.append(line)
            counter += 1

    task_to_be_deleted = input('Введите номер задачи, что вы хотите удалить: ')

    if task_to_be_deleted.isdigit() and 0 < int(task_to_be_deleted) <= len(current_task_list):
        task_to_be_deleted = current_task_list.pop(int(task_to_be_deleted) - 1)

        curr_date = datetime.date.today()

        print(f'ЗАДАЧА {task_to_be_deleted[-1]} БЫЛА УДАЛЕНА {curr_date}')

        with open('list_of_current_tasks.csv', 'w', newline='', encoding='utf-8') as file:
            task = csv.writer(file, delimiter='\t')
            for elem in current_task_list:
                task.writerow(elem)

    else:
        print('Введено некорректное значение')
