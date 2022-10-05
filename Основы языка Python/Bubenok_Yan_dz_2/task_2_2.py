
list_raw = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_new = []
for word in list_raw:
    digit = word
    sign = ''

    if len(digit) > 1:
        if digit[0] == '+':
            digit = digit[1:]
            sign = '+'
        if digit[0] == '-':
            digit = digit[1:]
            sign = '-'

    if digit.isdigit():
        list_new.append('"')
        list_new.append(f"{sign}{int(digit):02d}")
        list_new.append('"')
    else:
        list_new.append(word)

print(list_new)

string_from_list = ''
is_quote_open = False
for item in list_new:
    string_from_list += item

    if item == '"':
        is_quote_open = not is_quote_open

    if not is_quote_open:
        string_from_list += ' '

string_from_list = string_from_list[:-1]

print(string_from_list)



"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
"""

