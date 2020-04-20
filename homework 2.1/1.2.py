def bracket_check(test_string):
    if test_string == '':
        print('YES')
    else:
        check = 0
        exitcheck = False
        while test_string != '':
            for elem in test_string:
                if elem == '(':
                    check += 1
                    test_string = test_string[1::]
                else:
                    check -= 1
                    test_string = test_string[1::]
                    if test_string == '':
                        exitcheck = True
                if check < 0 or exitcheck == True:
                    break
            break
        if check != 0:
            print('NO')
        else:
            print('YES')

bracket_check('')