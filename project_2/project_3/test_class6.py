class Animal:

    def __init__(self, name, height, weight) -> None:
         self.name = name
         self.height = height
         self.weight = weight
       



class Dog(Animal):

    def __init__(self,voice, *args, **kwargs) -> None:
        self.voice = voice
        super().__init__(*args, **kwargs)



class Cat(Animal):

    def __init__(self,voice, *args, **kwargs) -> None:
        self.voice = voice
        super().__init__(*args, **kwargs)


p1 = Dog('Лает','Бим', 1, 25)
print(f'{p1.voice=}')

p2 = Cat('Мяукает','Барсик', 1, 25)
print(f'{p2.voice=}')



class Factory:
    # animal = Animal
    def __init__(self, animal, *args, **kwargs) -> None:#Принимает тип и параметры этого типа
        self.animal = Animal
      

    def ret_ins(self):
        p3 =  self.animal('слон', 3, 2000)#Внутри класса создаем экземпляр
        return p3#Возвращаем экземпляр
    
p4 = Factory(Animal)
print(p4.ret_ins())#ПОЧЕМУ ВЫВОД ТАКОЙ  <__main__.Animal object at 0x00000202D3F0BC40> И КАК СДЕЛАТЬ НОРМАЛЬНЫЙ ВЫВОД ПОЛУЧИВШЕГОСЯ ЭКЗЕМПЛЯРА 

   

   



        



        
