def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    elif len(coefficients) == 1:
        return [0 / coefficients[0]]
    elif len(coefficients) == 2:
        return [-coefficients[1] / coefficients[0]]
    elif len(coefficients) == 3:
        discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
        if discriminant > 0:
            return [(-coefficients[1] + discriminant ** 0.5) / 2 * coefficients[0], (-coefficients[1] - discriminant ** 0.5) / 2 * coefficients[0]]
        elif discriminant == 0:
            return [(-coefficients[1] + discriminant ** 0.5) / 2 * coefficients[0]]
        else:
            return None


print(sorted(solve(1, -3, 2)))