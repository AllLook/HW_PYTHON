import os
from pathlib import Path
import argparse
from collections import namedtuple
from logger_info import log_all


def re_file(dir_name):
    # dir_name = input("Укажите путь до директории:")
    if os.path.isdir(dir_name):  # само определяет как выставить слеши в пути
        obj_list = []

        p = Path(dir_name)  # инфо из текущей директории
        for obj in p.iterdir():  # перебор из этой директории
            # print(obj)
            obj = str(obj).lower().split('\\')  # приведение к нижнему регистру т.к расширение может быть заглавным
            # print(obj)
            if '.' in obj[-1]:  # если в последнем элементе из директории есть точка значит есть и расширение
                temp_obj = obj[-1].split('.')  # разделяем элемент по этой точке
                end_ex = temp_obj[-1]  # Будет расширением
                name_file = temp_obj[0]  # Будет именем файла
                obj.pop(-1)  # Будет родительской директорией для файла или папки
                temp = ('\\'.join(obj), name_file, end_ex)  # собираем кортеж данных,ведь изменения в пути не вносим
                obj_list.append(temp)  # добавляем в список результат из текущей директории
            else:
                name_file = 'false'  # Вместо флагов если нет расширений
                end_ex = 'false'
                obj.pop(-1)
                temp = ('\\'.join(obj), name_file, end_ex)
                obj_list.append(temp)
        copy_name_list = []  # Будет лист экземпляров
        print(obj_list)
        for item in obj_list:
            a, b, c = item  # Распоковываем  каждый кортеж на значения
            DIR_LIST = namedtuple('DIR_LIST', ['dir', 'file', 'exeption'])  # Делаем класс со свойствами
            copy_name = DIR_LIST(a, b, c)  # создаем его экземпляр
            copy_name_list.append(copy_name)  # добавляем в список экземпляров
            log_all()  # Вызываем логирование
        print(f'Список экземпляров: {copy_name_list}')
        return copy_name_list  # Возвращаем результат


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parsing files and directories')  # создание парсера
    parser.add_argument('param', metavar='String_patch', type=str, nargs=1,
                        help='files and directories')  # аргументы и их типы передаем в парсер
    args = parser.parse_args()  # принимаем результат работы парсера
    re_file(*args.param)  # вызываем функцию с переданными из парсера параметрами
