import sys
from user_class import User


def name_user():
    p1 = User('ivan', 'id123', 1)
    return p1


def copy_list():
    copy_class_list = []
    return copy_class_list


result = copy_list()


def users_list() -> list:
    i = 1
    while True:
        temp = input(
            'Введите по порядку через пробел: имя пользователя, id пользователя, уровень доступа от 1 до 7, введите compare чтобы сравнить профили или для выхода введите exit\n').lower().strip().split()

        if ''.join(temp) == 'compare':
            user1 = input('Введите обьект:')
            user2 = input('Введите обьект:')
            if user1 == user2:
                del user1
                print('Не может быть два одинаковых пользователя!Пользователь удален')
            else:
                print('Это разные пользователи!')

        elif ''.join(temp) == 'exit':
            User.__del__
            print('До свидания!')
            sys.exit()


        elif len(temp) == 3:
            name = temp[0]
            id = temp[1]
            level = temp[2]
            copy_name = 'u'
            copy_name = copy_name + str(i)
            print(copy_name)
            copy_name = User(name, id, level)
            print(copy_name)
            result.append(copy_name)
            i += 1
            print(f'Создан экземпляр класса {copy_name}')
            print(f'Список экземпляров {result}\n')

        else:
            print('Сделайте корректный ввод!')
            users_list()


if __name__ == '__main__':
    users_list()
