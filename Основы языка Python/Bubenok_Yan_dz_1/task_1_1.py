"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:


duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек duration = 400153
4 дн 15 час 9 мин 13 сек
Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?
"""

print('Convert seconds to days, hours and minutes\n')
# duration = int(input('Enter number of seconds to days, hours, minutes: '))

duration = [112987, 89456, 34098]
for last in duration:
    print('Duration =', last, 'seconds')
    days = last // 86400
    hours = last // 3600 % 24
    minutes = last // 60 % 60
    seconds = last % 60
    time = 'Time: '
    comma = ''
    if days:
        time += str(days) + ' days'
        comma = ', '
    if hours:
        time += comma + str(hours) + ' hours'
        comma = ', '
    if minutes:
        time += comma + str(minutes) + ' minutes'
        comma = ', '
    if seconds:
        time += comma + str(seconds) + ' seconds'
    time += '.'
    print(time, '\n')