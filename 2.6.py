def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    lst1 = []
    for j in range(m):
        lst2 = []
        for i in range(n):
            lst2 = lst2 + [matrix[i][j]]
        lst1 = lst1 + [lst2]
    matrix[:] = lst1


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
