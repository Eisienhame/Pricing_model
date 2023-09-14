from utils import import_csv_data, find_price


k = "csv_data_110.csv"
s = import_csv_data(k, 15)
print(s)
print(find_price(s))

