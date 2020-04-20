data = """o - x
o x x
x o o"""

field = [line.split() for line in data.split('\n')]

def tic_tac_toe(field):
    x = False
    o = False
    y1, y2, y3, di1, di2 = '', '', '', '', ''
    count = 0
    for elem in field:
        elem = ''.join(elem)
        count += 1
        if elem == 'xxx':
            x = True
        elif elem == 'ooo':
            o = True
        y1, y2, y3 = y1 + elem[0], y2 + elem[1], y3 + elem[2]
        if count == 1:
            di1, di2 = di1 + elem[0], di2 + elem[2]
        elif count == 2:
            di1, di2 = di1 + elem[1], di2 + elem[1]
        else:
            di1, di2 = di1 + elem[2], di2 + elem[0]
    if y1 == 'xxx' or y2 == 'xxx' or y3 == 'xxx' or di1 == 'xxx' or di2 == 'xxx':
        x = True
    if y1 == 'ooo' or y2 == 'ooo' or y3 == 'ooo' or di1 == 'ooo' or di2 == 'ooo':
        o = True
    if (x == False and o == False) or (x == True and o == True):
        print('draw')
    elif x == True and o == False:
        print('x win')
    elif x == False and o == True:
        print('o win')

tic_tac_toe(field)