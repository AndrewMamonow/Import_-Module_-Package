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