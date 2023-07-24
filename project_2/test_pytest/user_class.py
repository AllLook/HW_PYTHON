class User:
    def __init__(self, name, id, level) -> None:
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, other) -> bool:
        # return self.name == other.name and self.id == other.id and self.level == other.level
        first = self.id
        second = other.id
        return first == second  # ПОЧЕМУ НЕ РАБОТАЕТ СРАВНЕНИЕ В ОСНОВНОМ КОДЕ?ВСЕ ВАРИАНТЫ ПРОБЫВАЛ

    def __str__(self) -> str:
        return f'Экземпляр класса {User} c параметрами: {self.name}, {self.id}, {self.level}'

    def __del__(self):
        print('Удаление экземпляра класса')
