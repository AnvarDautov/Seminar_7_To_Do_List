import csv

def current_tasks():
    with open ('list_of_current_tasks.csv', 'r', encoding='utf-8') as file:
        task_list = csv.reader(file)
        for line in task_list:
            print (*line)


def done_tasks():
    with open ('list_of_done_tasks.csv', 'r', encoding='utf-8') as file:
        task_list = csv.reader(file)
        for line in task_list:
            print (*line)
