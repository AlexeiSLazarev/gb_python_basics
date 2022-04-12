'''
### 1. Реализовать вывод информации о промежутке времени в зависимости 
# от его продолжительности duration в секундах: до минуты: <s> сек; до часа: 
# <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: 
# <d> дн <h> час <m> мин <s> сек.
'''

# инициализируем необходимые данные
dividers = [24*60*60,60*60,60,1]
epoch_names = ['дн','час', 'мин' ,'сек']
res_list = []

def div_(val, div, res_list):
    # функция вычисления целых значений для дней, часов т.д.
    if val <= 0: return
    else:
        int_part = val//dividers[div]
        res_list.append(int_part)
        return div_(val - dividers[div]*int_part, div+1, res_list)
    
val = int(input('Введите длительность промежутка в секундах: '))
# вычисляем требуемые значения
div_(val, 0, res_list)
# приводим к нужному формату
l = [f'{value} {epoch_names[index]}' for index, value in enumerate(res_list) if value != 0]
# выводим результат на экран
print( 'Результат конвертации: ', ' '.join(l))