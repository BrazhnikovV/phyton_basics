from itertools import zip_longest
import json

out_put = {}

with open('files/users.csv', encoding='utf-8') as f_users:
    with open('files/hobby.csv', encoding='utf-8') as f_hobby:
        num_lines_users = sum(1 for line in f_users)
        num_lines_hobby = sum(1 for line in f_hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        # возвращаем указатель в начало после предыдущих итераций
        f_users.seek(0)
        f_hobby.seek(0)

        for line_user, line_user_hobby in zip_longest(f_users, f_hobby):
            out_put[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('files/tasks.json', 'w', encoding='utf-8') as f:
    json.dump(out_put, f, ensure_ascii=False)

print(out_put)
