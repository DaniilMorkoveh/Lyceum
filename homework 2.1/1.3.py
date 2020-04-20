def squared():
    st = ' '
    st0 = ''
    check = False
    for i in range(11, 100):
        if i % 10 == 0:
            pass
        else:
            if (i + 1) % 10 == 0:
                check = True
            else:
                pass
            i = str(i ** 2)
            if (len(i) == 3) and (check != True):
                i += st * 2
            elif (len(i) != 3) and (check != True):
                i += st
            else:
                pass
            st0 += i
            if check == True:
                print(st0)
                check = False
                st0 = ''
                continue
            else:
                continue

squared()