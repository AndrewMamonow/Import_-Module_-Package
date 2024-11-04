from prettytable import PrettyTable
from datetime import datetime, date, time
from application.db.people import get_employees
from application.salary import calculate_salary
from application.db.personals import personals

def table_print(table_title:list, table_list:list):
# Функция формирования таблицы для вывода   
    Pretty_table = PrettyTable()
    Pretty_table.field_names = table_title
    for item in table_list:
        Pretty_table.add_row(item)
    return Pretty_table

if __name__ == '__main__':
    current_date = datetime.now().strftime('%d.%m.%y')
    personal_list = [(get_employees(personal['id'], personals),
                    calculate_salary(personal['id'], personals),
                    '', current_date) for personal in personals]
    table_title = ["Фамилия", "Рассчитано", "Подпись", "Дата"]
    print(table_print(table_title, personal_list))
    item_sum = 0
    for item in personal_list:
        item_sum += int(item[1])
    print(f'Итого на {current_date} к выдаче {item_sum}')


