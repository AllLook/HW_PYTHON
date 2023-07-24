import sys
from exception_int_file import IntValueError

number = input("Введите целое число:")

try:
    number = int(number)
except:
    raise IntValueError(number)

if number <= 0 or number == 1 or number > 100000:
    print("Это число не подходит!")
    sys.exit()
i = 0
for j in range(2, number // 2 + 1):
    if number % j == 0:
        i += 1
if i == 0:
    print("Число простое!")
else:
    print("Число составное!")
