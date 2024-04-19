numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

results = [2,4,6,8]


for row in numbers:
    for number in row:
        if number % 2 == 0:
            results.append(number)


print("짝수:",results)