import os
from pathlib import Path
# #ЭТОТ ВАРИАНТ РАБОТАЕТ
# def re_file(name_file, in_ex, end_ex):
#     i = 0#ввод счетчика
#     for dir_main,dir_inside,file_name in os.walk(os.getcwd()):
#         for item in  file_name:
#             if item.endswith(in_ex):#проверка на расширение
#                 i += 1#прибавляем счетчик
#                 temp = item.split('.')
#                 temp[-1] = end_ex
#                 temp[0] = name_file + str(i)#новое имя + порядковый номер
#                 res_item = ''.join(temp)
#                 # if os.path.exists(res_item): #Пытался сделать проверку на существование такого файла с требуемым расширением и менять название рекурсией,но не срабатывает
#                 #     # def short_replace():
#                 #         temp2 = res_item.split('.')
#                 #         print(temp2)
#                 #         short =str(temp2[0])
#                 #         print(short)
#                 #         short = short.replace(short[-1],str(i + 1))
#                 #         temp2[0] = short
#                 #         print(temp2[0])
#                 #         res_item = '.'.join(temp2)
#                 #         print(res_item)
#                 #         if os.path.exists(res_item):
#                 #              short_replace()
#                 #         os.rename(item,res_item)#переименование 
#                 #         print(f'файл {item} переименован в {res_item}')  
#                 os.rename(item,res_item)#переименование 
#                 print(f'файл {item} переименован в {res_item}')
#     return 0 #отработала без ошибок
            
# print(re_file('000','.txt','.md'))


#ТАК ТОЖЕ РАБОТАЕТ
def re_file(name_file, in_ex, end_ex):
    i = 0
    p = Path(Path().cwd())#инфо из текущей директории
    for obj in p.iterdir():#перебор из этой директории
        print(obj)
        obj = str(obj).lower().split('\\')#приведение к нижнему регистру т.к расширение может быть заглавным
        if obj[-1].endswith(in_ex):
            i += 1
            temp_obj = obj[-1].split('.')
            temp_obj[-1] = end_ex
            temp_obj[0] = name_file + str(i)#новое имя + порядковый номер
            res_item = ''.join(temp_obj)
            Path(obj[-1]).rename(res_item)
            print(f'файл {obj[-1]} переименован в {res_item}')
        else:
            return -1

    return 0
        

 

print(re_file('000','.txt','.md'))






