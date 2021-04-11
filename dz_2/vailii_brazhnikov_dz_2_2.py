words_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx in range(len(words_list)):
    if words_list[idx].isnumeric():
        words_list[idx] = words_list[idx].zfill(2)
    else:
        tmp_parts_word = words_list[idx].split("+")
        if len(tmp_parts_word) > 1:
            words_list[idx] = tmp_parts_word[1].zfill(2)

print(words_list)
