class Matrix:
    """Класс для работы с матрицей."""
    # Просто проба,но тогда не работает __eq__ т.к один id только название меняется))
    # _instance = None#защищенная переменная для условия
    # def __new__(cls, *args, **kwargs):# __new__ служит для особого поведения класса или переназначения поведения? Все время дает true при сравнении,экземпляр один и тот же получается
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance#возвращаем экземпляр

    def __init__(self, matrix1) -> None:
        """Конструктор класса."""
        self.matrix1 = matrix1

    def __str__(self) -> str:
        """Представление для пользователя."""
        return f'Экземпляр класса {Matrix}, атрибут {self.matrix1=}'

    def __eq__(self, other) -> bool:
        """Сравнение для экземплярров класса."""
        first = self.matrix1
        second = other.matrix1
        return first == second

    def __add__(self, other):
        """Сложение для экземплярров класса."""
        first = self.matrix1
        second = other.matrix1
        # первый zip справа достает списки попарно,второй zip из них элементы и суммирует
        res = [map(sum, zip(*i)) for i in zip(first, second)]
        result = []
        for item in res:
            item = list(item)
            result.append(item)
        return Matrix(result)

if __name__ == '__main__':
    p1 = Matrix([[1, 1, 4], [3, 4, 5]])
    print(p1)
    p2 = Matrix([[1, 1, 4], [3, 4, 5]])
    p3 = p1 + p2
    print(p3)
    p4 = p1 == p2
    print(p4)
    help(Matrix)
    help(p1)
    print(Matrix.__doc__)
    help(p1.__add__)
