"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture()
def item_pc():
    return Item("ПК", 15000, 2)


@pytest.fixture()
def item_tablet():
    return Item("Планшет", 10000, 3)


def test_init(item_pc):
    assert item_pc.name == "ПК"
    assert item_pc.price == 15000
    assert item_pc.quantity == 2


def test_name(item_pc):
    item_pc.name = "Смартфон"
    assert item_pc.name == "Смартфон"


def test_calculate_total_price(item_pc):
    assert item_pc.calculate_total_price() == 30000


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == "Смартфон"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item_pc):
    assert repr(item_pc) == "Item('ПК', 15000, 2)"


def test_str(item_pc):
    assert str(item_pc) == 'ПК'


def test_add(item_pc, item_tablet):
    assert item_pc + item_tablet == 5
    with pytest.raises(ValueError, match=r"Складывать можно только объекты Item и дочерние от них."):
        item_pc + 5

