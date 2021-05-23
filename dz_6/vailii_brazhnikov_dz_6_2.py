with open('nginx_logs.txt') as f_open:
    data = []
    spammers = {}
    for line in f_open:
        splitted = line.split()
        data.append((splitted[0],splitted[5].replace('"',''), splitted[6]))
        spammers.setdefault(splitted[0], 0)
        spammers[splitted[0]] += 1

spammers = sorted(spammers.items(), key=lambda x: x[1], reverse=True)
print(spammers[:5])
