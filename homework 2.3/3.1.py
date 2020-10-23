def find_farthest_orbit(list_of_orbits):
    planets = {}
    square = []
    for i in range(len(list_of_orbits)):
        if list_of_orbits[i][0] == list_of_orbits[i][1]:
            break
        length = list_of_orbits[i][0] * list_of_orbits[i][1] * 3.1415926535
        planets[length] = list_of_orbits[i]
        square.append(length)
    square.sort()
    return planets[square[-1]]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))