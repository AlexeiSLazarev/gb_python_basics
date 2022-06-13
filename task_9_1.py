'''
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, 
жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, 
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном 
порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import os
import time

class TrafficLight:
    def __init__(self) -> None:
        self.color = 'red'
        self.running = False
        self.counter = 0
        # self.run()

    def run(self):
        self.counter == 0
        while True:
            if self.counter >= 3: 
                break
            if self.color == 'red':
                print('red')
                time.sleep(7)
                self.color = 'yellow'
            elif self.color == 'yellow':
                print('yellow')
                time.sleep(2)
                self.color = 'green'
            elif self.color == 'green':
                print('green')
                time.sleep(3)
                self.color = 'red'
            self.counter +=1
        
    def set_color(self, color):
        self.color = color
        z=1

# tl = TrafficLight()
# tl.run()

tl = TrafficLight()
tl.set_color('yellow')
tl.run()

z = 1