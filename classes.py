class Product:
    "Класс продукта"
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'продукт {self.name} будет иметь цену: {self.price}'

    def __str__(self):
        return self.name

