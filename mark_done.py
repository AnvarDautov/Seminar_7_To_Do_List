import csv
import datetime


def mark_done():
    print('СПИСОК ТЕКУЩИХ ЗАДАЧ:')
    with open('list_of_current_tasks.csv', 'r', encoding='utf-8') as file:
        task_list = csv.reader(file, delimiter='\t')
        current_task_list = []
        counter = 1
        for line in task_list:
            print(counter, line[-1], sep=' ')
            current_task_list.append(line)
            counter += 1
    done_task = input('Введите номер выполненной задачи: ')
    if done_task.isdigit() and 0 < int(done_task) <= len(current_task_list):
        done_task = current_task_list.pop(int(done_task) - 1)
        done_task_date = datetime.date.today()
        with open ('list_of_done_tasks.csv', 'a', newline='', encoding='utf-8') as file:
            task = csv.writer(file, delimiter = '\t')
            task.writerow((done_task_date, done_task[-1]))
        print(f'ЗАДАЧА {done_task[-1]} ВЫПОЛНЕНА {done_task_date}')
        with open ('list_of_current_tasks.csv', 'w', newline='', encoding='utf-8') as file:
            task = csv.writer(file, delimiter = '\t')
            for elem in current_task_list:
                task.writerow(elem)
    else:
        print('Введено некорректное значение')


