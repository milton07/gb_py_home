#Задание №1/2
print('Задание №1/2')

NUMBERS = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(num):

    for eng, rus in NUMBERS.items():
        if eng == num:
            return rus
        elif eng.title() == num:
            return rus.title()


print(num_translate('six'))
print(num_translate('One'))

#Задание №3

print('Задание №3')

def thesaurus(*args):
    names = {}
    let = []

    for name in args:
        let.append(name[0])
    let = list(set(let))
    let.sort()

    for let in let:
        list_names = []
        for name in args:
            if name[0] == let:
                list_names.append(name)
        names[let] = list_names
    return names


names = ['Иван', 'Мария', 'Пётр', 'Илья', 'Маргарита', 'Илёр']
print(thesaurus(*names))


#Задание №5

print('Задание №5')

from random import choice, shuffle


def get_jokes(num=1, repeat=False):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_jokes = []
    for joke in range(num):
        list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_jokes

print(get_jokes(repeat=True, num=3))
