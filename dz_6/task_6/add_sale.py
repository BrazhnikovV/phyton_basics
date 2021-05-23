import sys

price = sys.argv[1]

with open('dz_6/files/bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')
