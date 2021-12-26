from datetime import date
from application.salary import calculate_salary as calc_salary
from application.people import get_employees

if __name__ == '__main__':
    today = date.today().strftime('%d.%m.%Y')

    print('date now:', today)
    print('salary def:', calc_salary())
    print('employees def:',get_employees())
    

# 3)Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.


# 4) Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции (необязательное задание)
# from package import *