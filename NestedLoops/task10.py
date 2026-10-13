A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

rows = len(A)
cols = len(A[0])

result = []

for i in range(rows):
    row = []

    for j in range(cols):
        row.append(A[i][j] + B[i][j])

    result.append(row)

for row in result:
    print(row)
