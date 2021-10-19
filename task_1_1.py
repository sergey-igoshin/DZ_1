"""
DZ 1
Реализовать вывод информации о промежутке времени
в зависимости от его продолжительности duration в секундах:
a) до минуты: <s> сек;
b) до часа: <m> мин <s> сек;
c) до суток: <h> час <m> мин <s> сек;
d) * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""
while True:
    duration = int(input('Введите кол-во секунд: '))

    message = ''
    minute = 60
    hour = minute * 60
    day = hour * 24

    s = duration % 60
    m = duration // minute % 60
    h = duration // hour % 24
    d = duration // day

    if d > 0:
        print(f'{d} дн {h} час {m} мин {s} сек')
    elif h > 0:
        print(f'{h} час {m} мин {s} сек')
    elif m > 0:
        print(f'{m} мин {s} сек')
    else:
        print(f'{s} сек')

    # Вывод с использованием цикла
    array = [[d, 'дн '], [h, 'час '], [m, 'мин '], [s, 'сек']]
    for item in array:
        if item[0] > 0:
            message += str(item[0]) + ' ' + item[1]
    print(message)
