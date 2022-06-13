'''
4. Написать декоратор с аргументом-функцией (callback), позволяющий 
валидировать входные значения функции и выбрасывать исключение 
ValueError, если что-то не так, например:

def val_checker...
    ...
@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3
>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
'''

def my_decorator(input_arg):
 
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            # return result
            val = args[0]
            if input_arg(val):
                result = function(val)
                return result
            else:
                raise ValueError(val)
        return wrapper
    return the_real_decorator

@my_decorator(lambda x: x>0)

def calc_cube(x):
   return x ** 3
 
print(calc_cube(3))