def num_translate_adv(num):
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
    if num[0] == num[0].upper():
        num = num.lower()
        return num_words[num].capitalize()
    else:
        return num_words[num]

print(num_translate_adv("seven"))
print(num_translate_adv("Seven"))
