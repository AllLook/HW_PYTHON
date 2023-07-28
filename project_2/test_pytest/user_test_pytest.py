import pytest
import user_test
from user_class import User


def test_list():  # ожидается ошибка
    res = user_test.copy_list()
    assert type(res) == int, 'Неверный тип обьекта!'


@pytest.fixture()
def data():
    res2 = user_test.copy_list()
    return res2


def test_data(data):  # ожидается верный вывод
    data.append('name')
    assert data == ['name'], 'Ошибка значения'


def test_name():
    name_us = user_test.name_user()
    assert type(name_us) == User, 'Ошибка класса'


def test_name2():
    name_us = user_test.name_user()
    assert type(name_us) == str, 'Ошибка класса'


if __name__ == '__main__':
    pytest.main(['-v'])
