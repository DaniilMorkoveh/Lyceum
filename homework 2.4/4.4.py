from itertools import permutations


line1 = 'привет ток кот моток места ночь ночи есть тесть геолокация Надя'
line2 = 'Привет Доехали до места к ночи Здесь есть кот гладим его Даня'
nline1 = line1.lower().split()
nline2 = line2.lower().split()
for i in range(len(nline2)):
    for line in permutations(nline2[i], len(nline2[i])):
        if (''.join(line) in nline1) and (''.join(line) not in nline2):
            nline2[i] = ''.join(['#' for j in range(len(nline2[i]))])
            break
print(' '.join(nline2))