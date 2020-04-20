abc = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def tup(cell):
    cell = (abc.index(cell[0]), cell[1])
    return cell

def tupnot(cell):
    cell = str(abc[cell[0]]) + str(cell[1])
    return cell

def board_check(cell):
    if int(cell[0]) < 9 and int(cell[1]) < 9 and int(cell[0]) > 0 and int(cell[1]) > 0:
        return True
    else:
        return False

def possible_turns(cell):
    cell = tup(cell)
    turns = []
    for i in range(8):
        cell_check = cell
        if i == 0:
            cell_check = (int(cell[0]) - 1, int(cell[1]) + 2)
        elif i == 1:
            cell_check = (int(cell[0]) + 1, int(cell[1]) + 2)
        elif i == 2:
            cell_check = (int(cell[0]) + 2, int(cell[1]) + 1)
        elif i == 3:
            cell_check = (int(cell[0]) + 2, int(cell[1]) - 1)
        elif i == 4:
            cell_check = (int(cell[0]) + 1, int(cell[1]) - 2)
        elif i == 5:
            cell_check = (int(cell[0]) - 1, int(cell[1]) - 2)
        elif i == 6:
            cell_check = (int(cell[0]) - 2, int(cell[1]) + 1)
        elif i == 7:
            cell_check = (int(cell[0]) - 2, int(cell[1]) - 1)
        if board_check(cell_check) == True:
            turns.append(tupnot(cell_check))
        else:
            pass
    return sorted(turns)


print(possible_turns('D4'))