'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать 
их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
'''

class WrongValue(Exception):
    def __init__(self, message):
        self.message = message

class Date:
    
    def __init__(self, date):
        self.day, self.month, self.year = date.split('-')
        dict = {0:'день', 1:'месяц', 2:'год'}
        d = '01-11-2021'
        for i, x in enum(map(int,d.split('-'))):
            print(dict[i], x)
        
    @classmethod
    def extract_data(self, date):
        dict_ = {0:'день', 1:'месяц', 2:'год'}
        for i, x in enumerate(map(int,date.split('-'))):
            print(dict_[i], x) 

    
    @staticmethod
    def validate_data(date):
        
        def value_checker(val):
            if val[0] == 'день' and val[1]> 31: raise WrongValue('Неправильный день!') # меньше 0 не проверяем -> ексепшн от int
            elif val[0] == 'месяц' and val[1]> 12: raise WrongValue('Неправильный месяц!')
            elif val[0] == 'год' and len(str(val[1])) != 4: raise WrongValue('Неправильный год!')
            else: return 1
        
        dict_ = {0:'день', 1:'месяц', 2:'год'}
        for i, x in enumerate(map(int,date.split('-'))):
            if value_checker([dict_[i], x]):
                print(dict_[i], x)        

Date.extract_data('20-11-2031')
Date.validate_data('20-11-2031')