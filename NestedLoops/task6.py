matrix = [
    [3, 8, 2],
    [4, 15, 6],
    [7, 1, 9]
]

largest = matrix[0][0]
max_row = 0
max_col = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            max_row = i
            max_col = j

print("Largest:", largest)
print("Row:", max_row)
print("Column:", max_col)
