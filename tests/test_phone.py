from src.phone import Phone
import pytest


@pytest.fixture()
def phone_ip():
    return Phone("iPhone 14", 120000, 5, 2)


def test_init(phone_ip):
    assert phone_ip.name == "iPhone 14"
    assert phone_ip.price == 120000
    assert phone_ip.quantity == 5
    assert phone_ip.number_of_sim == 2


def test_number_of_sim(phone_ip):
    phone_ip.number_of_sim = 1
    assert phone_ip.number_of_sim == 1


def test_repr(phone_ip):
    assert repr(phone_ip) == "Phone('iPhone 14', 120000, 5, 2)"
