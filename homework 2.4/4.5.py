from sys import stdin


matrix = []
for line in stdin:
    matrix.append(list(map(int, line.split())))
print(matrix)


additional_matrix = tuple(zip(*matrix[::-1]))
print(additional_matrix)


summa = sum(matrix[0])
if all([sum(cell) == summa for cell in matrix]):
    if all([sum(cell) == summa for cell in additional_matrix]):
        print('YES')
    else:
        print('NO')
else:
    print('NO')