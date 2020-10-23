def ask_password(login, password, success, failure):
    true_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter_of_vowels = 0
    login = login.lower()
    addlogin = list(login)
    password = password.lower()
    addpass = list(password)
    con_check = False
    vowels_check = False
    for letter in password:
        if letter in true_vowels:
            counter_of_vowels += 1
    for i in reversed(range(len(addlogin))):
        if addlogin[i] in true_vowels:
            addlogin.pop(i)
    for i in reversed(range(len(addpass))):
        if addpass[i] in true_vowels:
            addpass.pop(i)
    for i in range(len(addlogin)):
        if addlogin[i] == addpass[i]:
            continue
        else:
            con_check = True
            break
    if counter_of_vowels != 3:
        vowels_check = True
    if vowels_check:
        if con_check:
            err = 'EVERYTHING IS WRONG'
        else:
            err = 'WRONG NUMBER OR VOWELS'
    else:
        if con_check:
            err = 'WRONG CONSONANTS'
        else:
            err = 'Nothing'
            return success(err)
    return failure(err)


def main(login, password):
    err = ask_password(login, password, lambda err: err, lambda err: err)
    if err == 'Nothing':
        print(f'Привет, {login}')
    else:
        print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку:{err}.')


main('anastasia', 'nsyatos')
main('eugene', 'aanig')
ask_password('anastasia', 'nsyatos', lambda login: print('super'), lambda login, err: print('bad'
                                                                                            ' '))