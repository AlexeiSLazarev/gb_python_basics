'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>
'''

def type_logger(func):
    def wrapper(arg):
        t = type(arg)
        val = func(arg)
        return f"{val}: {t}"
    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

print(calc_cube(3))