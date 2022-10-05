
list_raw = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0
length = len(list_raw)
while index < length:
    word = list_raw[index]
    sign = ''

    if len(word) > 1:
        if word[0] == '+':
            word = word[1:]
            sign = '+'
        if word[0] == '-':
            word = word[1:]
            sign = '-'

    if word.isdigit():
        list_raw[index] = f"{sign}{int(word):02d}"
        list_raw.insert(index, '"')
        list_raw.insert(index + 2, '"')
        index += 2
        length += 2

    index += 1

print(list_raw)

"""
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.
"""