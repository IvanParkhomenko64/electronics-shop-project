"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture()
def item_pc():
    return Item("ПК", 15000, 2)


def test_init(item_pc):
    assert item_pc.name == "ПК"
    assert item_pc.price == 15000
    assert item_pc.quantity == 2


def test_name(item_pc):
    item_pc.name = "Смартфон"
    assert item_pc.name == "Смартфон"
    # item_pc.name = "Смартфонывмываываыаыаываывваыаываыыаыаыа"
    # assert item_pc.name == "Смартфон"


def test_calculate_total_price(item_pc):
    assert item_pc.calculate_total_price() == 30000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 8
    item1 = Item.all[0]
    assert item1.name == 'ПК'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
