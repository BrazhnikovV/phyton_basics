# c
# ==================================
cnt = 0
while cnt < 20:
    if cnt == 0 or (cnt >= 5):
        print(cnt, "процентов")
    elif cnt >= 2 and cnt <= 4:
        print(cnt, "процента")
    else:
        print(cnt, "процент")

    cnt += 1
