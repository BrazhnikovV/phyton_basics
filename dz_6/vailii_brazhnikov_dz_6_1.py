with open('nginx_logs.txt') as f_open:
    data = []
    for line in f_open:
        splitted = line.split()
        data.append((splitted[0],splitted[5].replace('"',''), splitted[6]))
print(data)
