import pytest

from utils import import_csv_data, find_price


def test_get_file_not_found_error():
    "Test исключения FileNotFoundError в связи с отсутствием файла"""
    assert import_csv_data('tyr.csv', 10) == print(f"По указанному пути файл отсутствует")


def test_instantiateCSVError():
    "Test исключения FileNotFoundError в связи с отсутствием файла"""
    assert import_csv_data('csv_data_bad.csv', 10) == print(f"Файл поврежден")


def test_find_price(item_test2):
    assert find_price(import_csv_data('csv_data_110.csv', 15)) == item_test2
