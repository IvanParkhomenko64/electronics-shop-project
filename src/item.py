import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else '_Файл item.csv поврежден_'

    def __str__(self):
        return f'{self.__class__.__name__}: Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []
    source = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = new_name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(Item.source, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        else:
            try:
                with open(Item.source, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    if len(reader.fieldnames) != 3:
                        raise InstantiateCSVError
            except InstantiateCSVError:
                print('InstantiateCSVError: Файл item.csv поврежден')
            else:
                with open(Item.source, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
