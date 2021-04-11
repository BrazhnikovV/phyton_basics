price_list = [12.45, 9.52, 80.2, 22.90, 57.8, 46.51, 97, 28.7, 120.05, 14.99, 10.1]

# A
# ##############################

for idx in range(len(price_list)):
    if len(str(price_list[idx]).split(".")) > 1:
        rubles = str(price_list[idx]).split(".")[0]
        penny  = str(price_list[idx]).split(".")[1].zfill(2)
        print(rubles, "руб. ", penny, "коп.")
    else:
        rubles = str(price_list[idx]).split(".")[0]
        print(rubles, "руб. ", "0".zfill(2), "коп.")

# B
# ##############################
price_list.sort()
print(price_list)


# C
# ##############################
price_list.sort()
price_list.reverse()
print(price_list)

# D
# ##############################
price_list.sort()
price_list.reverse()
for idx in range(len(price_list)):
    if idx < 5:
        print(price_list[idx])
