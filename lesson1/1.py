# определяем константы в секундах
one_min = 60
one_hour = 3600
one_day = 86400
one_week = 6048006
one_month = 2629743
one_year = 31556926

#ввод duration
duration = int(input('Введите продолжительность в секундах: '))

#вывод только в секундах
if duration < one_min:
    print('{} сек'.format(duration))
#вывод секунды + минуты
elif one_min <= duration and one_hour > duration:
    my_min = duration // one_min
    my_sec = duration % one_min
    print('{} мин {} сек'.format(my_min,my_sec))
#вывод секунды + минуты + часы
elif duration >= one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_min
    my_sec = duration % one_min
    print('{} час {} мин {} сек'.format(my_hour,my_min,my_sec))
#вывод секунды + минуты + часы + дни
elif duration >= one_day and duration < one_week:
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_min
    my_sec = duration % one_min
    print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_min, my_sec))
#вывод секунды + минуты + часы + дни + недели
elif duration >= one_month and duration < one_year:
    my_week = duration // one_week
    duration = duration % one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_min
    my_sec = duration % one_min
    print('{} нед {} дн {} час {} мин {} сек'.format(my_week, my_day, my_hour, my_min, my_sec))
#вывод секунды + минуты + часы + дни + недели + месяцы
elif duration >= one_year:
    my_year=duration // one_year
    duration = duration % one_year
    my_week = duration//one_week
    duration = duration % one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_min
    my_sec = duration % one_min
    print('{} год {} нед {} дн {} час {} мин {} сек'.format(my_year, my_week, my_day, my_hour, my_min, my_sec))

    
