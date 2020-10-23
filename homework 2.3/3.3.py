import math


def dots(beg, end, step):
    d1 = beg
    list_of_dots = []
    while d1 < end:
        list_of_dots.append(d1)
        d1 += step
    return list_of_dots


def distance(dot):
    return ((0.75 - dot[0]) ** 2 + (0 - dot[1]) ** 2) ** (1 / 2)


coords = [(math.cos(3 * d), math.sin(3 * d)) for d in dots(0, 2 * 3.1415, 0.0001)]
distances = [round(distance(x), 4) for x in coords]
print(min(distances))