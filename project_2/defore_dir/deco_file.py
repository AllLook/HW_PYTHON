import random as rnd
import csv
import json


def deco1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


def square_roots(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = -b + d ** 0.5 / 2 * a
        x2 = -b - d ** 0.5 / 2 * a
        return x1, x2
    elif d == 0:
        x1 = x1 = -b + d ** 0.5 / 2 * a
        return x1
    else:
        return 'Not square'


def num_gen(n: int):
    temp_dct = {}
    i = 0
    temp = []
    while i < n:
        temp.append(rnd.sample(range(n), 3))
        i += 1
    with (
        open('num_file.csv', 'w', newline='', encoding='utf-8') as f
    ):
        csv_write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for item in temp:
            csv_write.writerow(item)

    with (
        open('num_file.csv', 'r', newline='', ) as f
    ):
        csv_file = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for line in csv_file:
            a, b, c = line
            # Json не принял кортежи в качестве ключа
            temp_dct[str(line)] = square_roots(a, b, c)
    return temp_dct

if __name__ == '__main__':
    control = deco1(num_gen)
    print(control(100))


    @deco1
    def write_json():
        with (
            open('res_json.json', 'w') as f_j
        ):
            json.dump(num_gen(100), f_j)


    write_json()
