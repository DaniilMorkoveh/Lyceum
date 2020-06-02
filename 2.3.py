d = {}


def add_friends(nameOfPerson, listOfFriends):
    key_check = False
    d0 = {nameOfPerson: listOfFriends}
    global d
    for key in d.keys():
        if key == nameOfPerson:
            key_check = True
        if key_check == True:
            break
    if key_check == False:
        d.update(d0)
    else:
        lst = d.get(nameOfPerson)
        for elem in listOfFriends:
            lst.append(elem)
        d1 = {nameOfPerson: lst}
        d.update(d1)


def is_friends(nameOfPerson1, nameOfPerson2):
    check = False
    global d
    lst = d.get(nameOfPerson1)
    for elem in lst:
        if elem == nameOfPerson2:
            check = True
        if check == True:
            break
    return check


def print_friends(nameOfPerson):
    global d
    lst = d.get(nameOfPerson)
    lst.sort()
    print(' '.join(lst))


add_friends('Алла', ['Марина', 'Иван'])
print(is_friends('Алла', 'Мария'))
add_friends('Алла', ['Мария'])
print(is_friends('Алла', 'Мария'))
print_friends('Алла')
