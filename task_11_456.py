'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в 
определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.
'''

class Storage:
    
    def __init__(self, capacity_value):
        self.max_capacity = capacity_value
        self.capacity_left = capacity_value
        self.items = []
    
    def check_item_info(self, item_info):
        try:
            int(item_info[0])
            return 1
        except:
            print('Кол-во техники должно быть численным значением')
            
    def add_item(self, item_info, value):
        # item_info = кол-во, подразделение в компании
        if self.check_item_info(item_info):
            if self.capacity_left - value > 0:
                self.items.append(item_info)
                self.capacity_left -= value
            else: 
                print('Недостаточно места для хранения')
    def print_item_list(self):
        print(self.items)
            

class OfficeEquipment():

    def __init__(self, power_consumption, working_state, price, init_date, users):
        self.power_consumption = power_consumption
        self.working_state = working_state
        self.price = price
        self.init_date = init_date
        self.users = users
    
class Printer(OfficeEquipment):
    
    def __init__(self, printing_cartrige_capacity):
        self.printing_cartrige_capacity = printing_cartrige_capacity
        self.pages_printed = 0
    
    def print_pages(self, pages_to_print):
        self.pages_printed += pages_to_print
        self.printing_cartrige_capacity -= pages_to_print
        
class Scanner(OfficeEquipment):
    
    def __init__(self, scan_speed):
        self.scan_speed = scan_speed
    
    def scan_page(self, page):
        pass

class Xerox(OfficeEquipment):
    
    def print_copy(number_of_copyes):
        pass

s = Storage(100)
s.add_item([19,'Отдел 1'], 90)
s.print_item_list()    


