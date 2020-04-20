def password_level(password):
    check1 = check2 = check3 = False
    digits = '0123456789'
    for elem in password:
        if elem in digits:
            check1 = True
        if elem.isupper():
            check2 = True
        if elem.islower():
            check3 = True
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif password.isdigit():
        return 'Ненадежный пароль'
    elif check2 ^ check3 and not check1:
        return 'Ненадежный пароль'
    elif check1 * check2 * check3:
        return 'Надежный пароль'
    else:
        return 'Слабый пароль'
print(password_level('Qwerty'))