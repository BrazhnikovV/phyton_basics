import re

EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, addr = EMAIL.findall(email)[0]
    else:
        raise ValueError('wrong email: {email}')
    print(name, addr)

email_parse('brazhnikov@yandex.ru')
email_parse('brazhnikov@yandex')

