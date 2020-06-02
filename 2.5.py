def fractal_print(lst):
    print('[' + ', '.join(map(str, lst)) + ']')


fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)