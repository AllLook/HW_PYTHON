class ExaminationValueError(Exception):
    pass


class CheckValueError(ExaminationValueError):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        text = ''
        if self.a == 0 or self.b == 0 or self.c == 0:
            text = 'Стороны не могут быть равны 0!'
        elif self.a < 0 or self.b < 0 or self.c < 0:
            text = 'Стороны не могут быть меньше 0!'

        elif self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
            text = 'Такого треугольника не существует!Одна из сторон не может быть более суммы двух других'
        return text
