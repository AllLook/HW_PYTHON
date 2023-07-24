from examination_value_error import CheckValueError

a = int(input("Введите сторону треугольника:"))
b = int(input("Введите сторону треугольника:"))
c = int(input("Введите сторону треугольника:"))
if a == 0 or b == 0 or c == 0:
    raise CheckValueError(a, b, c)
elif a < 0 or b < 0 or c < 0:
    raise CheckValueError(a, b, c)
# if a <= 0 or b <= 0 or c <= 0:
#     raise CheckValueError(a, b, c)  # ТАК НЕ РАБОТАЕТ ВЫДАЕТ НЕ ТОТ ТЕКСТ КОТОРЫЙ НАДО
elif a > b + c or b > a + c or c > a + b:
    raise CheckValueError(a, b, c)
elif a != b and b != c and c != a:
    print("Разностороний треугольник!")
elif a == b != c or b == c != a or a == c != b:
    print("Треугольник равнобедренный!")
else:
    print("Равносторонний треугольник!")
