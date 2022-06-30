from input_task import task_input
from mark_done import mark_done
from view_tasks import current_tasks
from view_tasks import done_tasks
from user_menu import menu_interface
from delete_task import delete_task
from change_task import change_task

def to_do_list():
    user_input = 'random'
    while user_input != '7':
        menu_interface()
        user_input = input("Выберите пункт из меню: ")
        if user_input == '1':
            task_input()
        elif user_input == '2':
            mark_done()
        elif user_input == '3':
            current_tasks()
        elif user_input == '4':
            done_tasks()
        elif user_input == '5':
            delete_task()
        elif user_input == '6':
            change_task()
        elif user_input not in '1234567':
            print('Введено некорректное значение. Попробуйте еще раз. ')
    else: print('До свидания!')

to_do_list()


                    