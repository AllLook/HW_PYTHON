class ValueIntException(Exception):
    pass


class IntValueError(ValueIntException):
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'Возникла ошибка!Повторите ввод корректного числа!'
