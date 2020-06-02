scoring = {1: [8, 2], 2: [6, 9], 3: [42, 56], 20: [50, 3]}


def score(*args):
    global scoring
    if len(args) == 1:
        if args[0] == 'Яблочко':
            return 50
        elif args[0] == 'Зеленое кольцо':
            return 25
    else:
        if args[0] == 'Внешнее кольцо':
            return scoring[args[1]][0]
        elif args[0] == 'Внутреннее кольцо':
            return scoring[args[1]][1]


print(score('Внешнее кольцо', 1))