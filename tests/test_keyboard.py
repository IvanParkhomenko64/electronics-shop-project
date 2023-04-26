import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard_asus():
    return Keyboard("For PC ASUS", 5000, 2)


def test_init(keyboard_asus):
    assert keyboard_asus.name == "For PC ASUS"
    assert keyboard_asus.price == 5000
    assert keyboard_asus.quantity == 2
    assert keyboard_asus.language == 'EN'

def test_change_lang(keyboard_asus):
    keyboard_asus.change_lang()
    assert keyboard_asus.language == 'RU'
    keyboard_asus.change_lang()
    assert keyboard_asus.language == 'EN'
