# a
# ==================================
cubes = []
cnt = 0
while cnt < 1000:
    if cnt % 2:
        cubes.append(cnt ** 3)
    cnt += 1

summa = 0;
for cube in cubes:
    if (cube % 7) == 0:
        summa += cube

print(summa)

# b
# ==================================
for idx in range(len(cubes)):
    cubes[idx] += 17

summa = 0;
for cube in cubes:
    if (cube % 7) == 0:
        summa += cube

print(summa)
