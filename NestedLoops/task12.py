matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

n = len(matrix)
symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

    if not symmetric:
        break

if symmetric:
    print("Symmetric")
else:
    print("Not symmetric")
