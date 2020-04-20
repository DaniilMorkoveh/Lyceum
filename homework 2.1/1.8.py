def make_shades(alley, k):
    alley1 = []
    for elem in alley:
        elem = False
        alley1.append(elem)
    for elem in alley:
        elem = int(elem)
        count = 0
        if k == 0:
            if elem != 0:
                alley1[alley.index(str(elem))] = True
        if k == 1:
            if elem != 0:
                while count != (elem + 1):
                    if alley1[-1] == True:
                        break
                    alley1[alley.index(str(elem)) + count] = True
                    count += 1
        if k == -1:
            if elem != 0:
                while count != (elem + 1):
                    if alley1[-1] == True:
                        break
                    alley1[alley.index(str(elem)) - count] = True
                    count += 1
    return alley1


def calculate_sunny_length(shades):
    count = 0
    for elem in shades:
        if elem == False:
            count += 1
        else:
            pass
    return count


def main():
    k = int(input())
    alley = input()
    alley = alley.split()
    if calculate_sunny_length(make_shades(alley, k)) < 10:
        print('Тени достаточно')
    else:
        print('Обгорел')


main()