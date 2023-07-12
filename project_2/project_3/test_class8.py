class Person_premium:
    name_ = ["Иван", "Петр", "Михаил", "Виктор"] #атрибуты класса
    bid = [10000, 15000, 20000, 30000]
    premium = ['10.25%', '10.25%', '10.25%', '10.25%']

    def name_prem(self,name_, bid, premium):#метод внутри класса
        for i in range(len(premium)):
            for item in premium:
                item = str(item).replace('%', '')
                premium[i] = float(item)
   
        # генератор множества
        res_set = {it / 100 * it2 for it in bid for it2 in premium}
        # генератор словаря
        res_dict = {
            res_key: res_value for res_key in name_ for res_value in res_set}
       
        print(res_dict)
   


p1 = Person_premium()#получаем экземпляр класса
print(p1.name_prem(["Иван", "Петр", "Михаил", "Виктор"], [10000, 15000, 20000, 30000], ['10.25%', '10.25%', '10.25%', '10.25%']))#задача решается через метод экземпляра