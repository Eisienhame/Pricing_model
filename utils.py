import csv


def import_csv_data(csv_data, good_count):
    """ Функ-ция принимает csv файл с данными и преобразует в оформленный список словарей, где ключом
    будет название продукта, а значения суммой цен и их кол-вом. Good_count необходим для настройки
     какого количества продаж не достаточно, чтобы учитывать цену в статистику"""
    with open(csv_data, encoding='utf-8') as r_file:
        names_product = []
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        # Считывание данных из CSV файла
        for row in file_reader:
            need_key = False
            # проверка, если первая строчка с шапкой названий или неверно заполненные данные
            # больше good_count убирает маленькое кол-во продаж
            if row[0].isdigit() and row[1].isdigit() and (int(row[1]) > good_count):
                if len(names_product) != 0:
                    for i in names_product:
                        for k, v in i.items():
                            if k == row[4]:
                                v[0] = v[0] + int(row[0])
                                v[1] += 1
                                need_key = True

                if (len(names_product) == 0) or (need_key is False):
                    data = {f'{row[4]}': [int(row[0]), 1]}
                    names_product.append(data)

            else:
                continue
    return names_product




