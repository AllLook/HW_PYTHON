# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов

#ПРОВЕРИЛ НА МАЛЕНЬКОЙ ДИРЕКТОРИИ

import json
import csv
import pickle
import os
from pathlib import Path


def defore_dir(dir_name):
    if os.path.isdir(dir_name):  # Если переданная директория существует
        res_dir = []

        for dir_main, dir_inside, file_name in os.walk(dir_name):
            # из переданной директории цикл срабатывает для каждой директории внутри до конца
            # {[ os.stat(i).st_size for i in file_name]}' не получилось вывести размер файлов stat не работает с лист,так тоже не получилось
            temp = f'Каталог {dir_main} содержит вложенные папки {dir_inside} длинной {len(dir_inside)} и файлы {file_name} длиной {len(file_name)}'
            # результат работы для каждой директории внутри помещаем в список
            res_dir.append(temp)
        with (
            open('list_json.json', 'w', encoding='utf-8') as f_json,
            # для excel на виндовс
            open('list_csv.csv', 'w', encoding='cp1251') as f_csv,
            open('list_pickle.pickle', 'wb') as pf
        ):

            json.dump(res_dir, f_json, ensure_ascii=False, indent=2)
            csv_write = csv.writer(f_csv, delimiter=' ', quotechar=' ')
            for item in res_dir:
                csv_write.writerow(item)
            pickle.dump(res_dir, pf)


if __name__ == '__main__':

    dir_name = input("Укажите путь до директории:").replace('/', '\\').strip()
    defore_dir(dir_name)
