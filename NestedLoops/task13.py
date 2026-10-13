matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = int(input("Enter target: "))
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print("Found at row:", i, "column:", j)
            found = True
            break

    if found:
        break

if not found:
    print("Not found")
