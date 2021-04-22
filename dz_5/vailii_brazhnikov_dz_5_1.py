def oddNumbersGenerator(input_number):
    for num in (num for num in range(1, input_number, 2)):
        yield num

print(*oddNumbersGenerator(134))
