'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, 
is_police(булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула 
(куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, 
PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно 
выводиться сообщение о превышении скорости.
'''

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.color} {self.name} поехала'

    def stop(self):
        return f'{self.color} {self.name} остановилась'

    def turn_right(self):
        return f'{self.color} {self.name} повернула направо'

    def turn_left(self):
        return f'{self.color} {self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} = {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')

        if self.speed > 60: return f'Скорость превышена!'
 

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость  {self.name} = {self.speed}')

        if self.speed > 40: return f'Скорость превышена!'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def get_info(self):
        if self.is_police:
            return f'Полицейская машина {self.color} {self.name}'
        else:
            return f'{self.color} {self.name}'


sc = SportCar(100, 'Белая', 'Ваз 2101', False)
tk = TownCar(30, 'Красный', 'автобус', False)
wk = WorkCar(70, 'Зеленый', 'грузовик', False)
pk = PoliceCar(110, 'Сине-белая',  'Lada Kalina', True)

print(sc.turn_left())
print(tk.stop())
print(wk.show_speed())
print(pk.get_info())