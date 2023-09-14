from utils import import_csv_data, find_price
from pathlib import Path
from classes import Product

menu_exit = True

while menu_exit:
    print("Здравствуйте, напишите полный путь до вашего файла с данными(в формате .csv)")
    print("Для выхода из программы напишите 'exit'")
    user_csv = input()
    print(user_csv)
    if user_csv.lower() == 'exit':
        menu_exit = False
        break
    if user_csv.endswith('csv') is False:
        print('Путь неправильный')
    else:
        count_sales = input('Введите какое минимальное кол-во продаж учитывается ')
        user_csv.replace("\\", "/")
        user_csv = str(Path(user_csv))
        needed_price = find_price(import_csv_data(user_csv, count_sales))
        print("Вот полученные результаты:")
        for i in needed_price:
            product = Product(i[0], i[1])
            print(product)

        print("Хотите продолжить работу? (пишите 'yes' или 'no')")
        answer = input()
        if answer.lower() == 'no':
            menu_exit = False
