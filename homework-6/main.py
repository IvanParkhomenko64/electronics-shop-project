from src.item import Item
import csv


if __name__ == '__main__':
    Item.source = '../src/_items_.csv'
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.source = '../src/items_.csv'
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
