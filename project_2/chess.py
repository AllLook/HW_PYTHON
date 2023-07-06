import random  as rd
def gen_num(num):
    temp1 = []
    temp2 = []
    for _ in range(num):
        x,y = rd.sample(range(num),2)
        temp1.append(x)
        temp2.append(y)
    print(temp1,temp2)
    

    result = True  # вводим логическую переменную для проверки
    for i in range(num):  # по длинне поля
        for j in range(i + 1, num):  # на следующий шаг
            # проверка на столкновение
            if temp1[i] == temp1[j] or temp2[i] == temp2[j] or abs(temp1[i] - temp1[j]) == abs(temp2[i] - temp2[j]):
                result = False
    win = 0
    win_res = []
    if result:
        print('NO')
        win = win + 1
        win_res.append(temp1)
        win_res.append(temp1)
        if win == 4:
            print(win_res)

    else:
        print('YES')

print(gen_num(8))
