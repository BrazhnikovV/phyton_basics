import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """Function return list jokes
    :param num:
    """
    cnt = 0
    joke_list = []
    while cnt < num:
        joke_str = random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives)
        joke_list.append(joke_str)
        cnt += 1
    return joke_list


def get_jokes_adv(num, repeat=False):
    """Function return list jokes
    :param num:
    :param repeat:
    """
    cnt = 0
    joke_list = []

    if not repeat:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_list.append(nouns[i] + " " + adverbs[i] + " " + adjectives[i])
    else:
        while cnt < num:
            joke_str = random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives)
            joke_list.append(joke_str)
            cnt += 1
    return joke_list

print(get_jokes(2))
print(get_jokes_adv(3, False))
