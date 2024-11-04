from package.module import *


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