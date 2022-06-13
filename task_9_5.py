'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), 
Handle (маркер);
в каждом классе реализовать переопределение метода draw. 
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный 
метод для каждого экземпляра.
'''

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки»')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'«Запуск отрисовки ручкой: {self.title}»')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'«Запуск отрисовки карандашом: {self.title}»')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'«Запуск отрисовки маркером: {self.title}»')


p = Pen('Синяя ручка')
pcl = Pencil('Красный карандаш')
hdl = Handle('Зеленый маркер')

p.draw()
pcl.draw()
hdl.draw()