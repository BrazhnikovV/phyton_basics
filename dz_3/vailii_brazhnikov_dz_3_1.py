def num_translate(num):

    num_words = {'one':   'один',
                 'two':   'два',
                 'three': 'три',
                 'four':  'четыре',
                 'five':  'пять',
                 'six':   'шесть',
                 'seven': 'семь',
                 'eight': 'восемь',
                 'nine':  'девять',
                 'ten':   'десять'}
    print(num_words.get(num))

num_translate("one")
num_translate("two")
num_translate("six")
