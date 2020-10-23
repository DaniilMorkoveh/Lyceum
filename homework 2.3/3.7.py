from sys import stdin


data = list(filter(lambda line: line.lstrip(), stdin))
for count, line in enumerate(data):
    if line.lstrip().startswith('#'):
        print(f'Line {count + 1}: {line.lstrip("#").strip()}')