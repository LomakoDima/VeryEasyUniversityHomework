matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:
    for element in row:
        total += element

print("Sum:", total)
