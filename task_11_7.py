'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и 
умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), 
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

import math

class Complex(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}{self.b}i'

    def __add__(self, rhs):
        return Complex(self.a + rhs.a, self.b + rhs.b)
    
    def __mul__(self, rhs):
        return Complex(self.a * rhs.a - self.b * rhs.b, self.a * rhs.b + self.b * rhs.a)
    

z_1 = Complex(10, -22)
z_2 = Complex(42, 3)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)