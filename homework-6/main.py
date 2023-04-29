from src.item import Item
import csv


if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден

    # with open('../src/items.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     print(len(reader.fieldnames))
