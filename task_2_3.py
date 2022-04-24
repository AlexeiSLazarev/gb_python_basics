'''
2. На вход будет выдаваться список, пример:

['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:

['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
b) Сформировать из обработанного списка строку:

в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    str_out = "здесь полученная после всех преобразования строковая переменная"
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

*(вместо задачи 2) Решить задачу 2, не создавая новый список (как говорят, in place). 
Эта задача намного серьёзнее, чем может сначала показаться.
'''

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def get_num_ids(my_list):
    num_ids = []
    for index,x in enumerate(my_list):
        if has_numbers(x): 
            num_ids.append(index)
    return num_ids

def process_digits(my_list,num_ids):
    for i in num_ids:
        if len(my_list[i])<2: my_list[i] = '0'+str(my_list[i])
        elif len(my_list[i]) == 2:
            digit_ind = get_digit_ind(my_list[i])
            if len(digit_ind) == 1: 
                my_list[i] = my_list[i][:digit_ind[0]] + '0' + my_list[i][digit_ind[0]:]
            
    return my_list

def update_commas(my_list,num_ids):
    while num_ids:
        i = num_ids.pop()
        my_list.insert(i,'"')
        my_list.insert(i+2,'"')
    return my_list

def get_digit_ind(dg_str):
    cntr = []
    for index, c in enumerate(dg_str):
        if c.isdigit(): cntr.append(index)
    return cntr
        
def convert_list_to_string(my_list):
    # my_list = my_list[::-1]
    result = ''
    flag_odd = True
    flag_first = False
    for x in my_list:
        if x == '"': 
            if flag_odd:
                result = result + ' ' + '\"'
                flag_first = True
            else: result = result + '\"'
            flag_odd = not flag_odd
        else:
            if flag_first:
                result = result + x
                flag_first = not flag_first
            else:
                result = result + ' '+ x
    return result
    
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
def convert_list_in_str(my_list):
    num_ids = get_num_ids(my_list)
    my_list = process_digits(my_list,num_ids)
    print('my_list:', my_list)
    print("my_list id: ", id(my_list))
    my_list = update_commas(my_list,num_ids)
    print('my_list:', my_list)
    print("my_list id: ", id(my_list))
    result = convert_list_to_string(my_list)
    return result
    

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('my_list:', my_list)
print("my_list id: ", id(my_list))
result = convert_list_in_str(my_list)
print("Конечный результат: ", result)