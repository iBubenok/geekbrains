"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""

list_cubes_odd = [number ** 3 for number in range(1, 1001) if number % 2]
# print(list_cubes_odd)
total = 0
for number in list_cubes_odd:
    decompose = number
    cumulative = 0
    while decompose > 0:
        cumulative += decompose % 10
        decompose = decompose // 10
    if cumulative % 7 == 0:
        total += cumulative
print('Результат задачи под пунктом a = ', total)

total = 0
for number in list_cubes_odd:
    decompose = number + 17
    cumulative = 0
    while decompose > 0:
        cumulative += decompose % 10
        decompose = decompose // 10
    if cumulative % 7 == 0:
        total += cumulative
print('Результат задачи под пунктом b = ', total)

