"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item_pc():
    return Item("ПК", 15000, 2)


def test_init(item_pc):
    assert item_pc.name == "ПК"
    assert item_pc.price == 15000
    assert item_pc.quantity == 2


def test_calculate_total_price(item_pc):
    assert item_pc.calculate_total_price() == 30000
