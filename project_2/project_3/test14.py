from collections import defaultdict
import csv


class Descriptor:  # создание дескриптора
    def __init__(self, name: str = None, surname: str = None):
        self.name = name
        self.surname = surname

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value.istitle() and value.isalpha() and value.istitle() and value.isalpha():
            pass
        else:
            raise ValueError(
                f'Проверьте значения name и surname передаваемые при создании экземпляра')


class Student:
    name = Descriptor()  # те свойства которые будут проверяться
    surname = Descriptor()

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.storage = defaultdict(list)

    def __call__(self, file: str):  # реализовано чтение файла через создание экземпляра
        with open(file, 'r', newline='') as f:
            csv_file = csv.reader(f, dialect='excel')
            for i, line in enumerate(csv_file):
                if i != 0:
                    self.storage[self.name, self.surname].append(line)

    def __str__(self) -> str:
        return f'Экземпляр класса {Student} с параметрами имя: {self.name}, фамилия: {self.surname}'

    @property
    def average(self):  # получаем средний был по оценкам
        res = 0
        i = 0
        for item in self.storage.values():
            for it in item:
                res += int(it[1])
                i += 1
        res = res // i
        return res


if __name__ == '__main__':
    p1 = Student('John', 'Wayne')
    print(p1)
    temp = input('Введите путь до файла:\n')
    for item in temp:
        if item == '\\':
            temp = temp.replace('\\', '/')
    p1(temp)
    print(p1.storage)
    print(f'Средняя оценка {p1.average}')
