matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

count = 0

for row in matrix:
    for element in row:
        if element % 2 == 0:
            count += 1

print("Even numbers:", count)
