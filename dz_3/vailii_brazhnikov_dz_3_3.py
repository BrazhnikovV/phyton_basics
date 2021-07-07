

def thesaurus(*names):
    map_names = {}
    for name in names:
        if map_names.get(str(name)[0]) is None:
            map_names[str(name)[0]] = []
            map_names[str(name)[0]].append(name)
        else:
            map_names[str(name)[0]].append(name)

    print(map_names)

thesaurus("Иван", "Мария", "Петр", "Илья")
