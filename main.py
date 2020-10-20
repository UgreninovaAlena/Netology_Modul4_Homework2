import ForTask_1
import ForTask_2

def Get_akt():
    print(f'Введите 1 для запуска задания 1')
    print(f'Введите 2 для запуска задания 2')
    print(f'Введите 0 для выхода')
    print()
    return input()

def work():
    akt = '1'
    while akt != '0':
        akt = Get_akt()
        if akt == '1':
            ForTask_1.task_1()
        elif akt == '2':
            ForTask_2.task2()

work()