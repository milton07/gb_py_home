# Задание 1
print('Задание №1')
# задаем выражения
form_1 = 15 * 3
form_2 = 15 / 3
form_3 = 15 * 2
form_4 = 15 ** 2

# выводим тип опцией type
print('form_1 type = ', form_1, type(form_1))
print('form_2 type = ', form_2, type(form_2))
print('form_3 type = ', form_3, type(form_3))
print('form_4 type =  ', form_4, type(form_4))


# Задание 2/3
print('Задание №2/3')

#исходный список
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# длина + id
lenght: int = len(list)
store_id = id(list)

# обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка,
# являющегося числом) и дополнить нулём до двух целочисленных разрядов
for i in range(lenght):
    entity = list.pop(0)
    if  entity.isdigit():
        list.append(F'"{int(entity):02d}"')
    elif entity[0] == "+" and entity[1].isdigit():
        list.append(F'"+{int(entity):02d}"')
    else:
        list.append(entity)
print(' '.join(list))

# Задание 4
print('Задание №4')

hello = 'Привет, {}!'

staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for correct_staff in staff:
    print(hello.format(correct_staff.split()[-1].title()))

# Задание 5
print('Задание №5')

#не успевал
