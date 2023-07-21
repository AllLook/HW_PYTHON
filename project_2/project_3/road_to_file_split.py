# Нужно вывести путь до директории отдельно,файл распарсить на название и расширение
temp = input("Введите путь к файлу:")
if '\\' in temp or '/' in temp:
    temp = temp.split('\\')
    *a, b = temp
    b = str(b).split('.')
    res = (a, b[0], b[1])
    print(res)
else:
    raise ValueError('Неправильный формат ввода!')
