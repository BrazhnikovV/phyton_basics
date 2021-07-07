def oddNumbersGenerator(input_number):
    return (num for num in range(1, input_number, 2))

print(*oddNumbersGenerator(15))
