def eratosthenes(N):
    lst1 = []
    lst2 = []
    if N < 4:
        return
    for i in range(2, N + 1):
        lst1.append(i)
    while lst1:
        for i in lst1[1:]:
            if i % lst1[0] == 0:
                lst2.append(i)
                lst1.remove(i)
        lst1 = lst1[1:]
    for i in lst2:
        print(i, end=' ')

eratosthenes(15)