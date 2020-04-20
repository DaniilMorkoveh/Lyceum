def middle_value(arr):
    return sum(arr) / len(arr)


def median_value(arr):
    arsrt = sorted(arr)
    index = (len(arr) - 1) // 2
    if len(arr) % 2:
        return arsrt[index]
    else:
        return (arsrt[index] + arsrt[index + 1]) / 2.0


def print_statistics(arr):
    if arr == []:
        for i in range(5):
            print(0)
    else:
        print(len(arr))
        print(middle_value(arr))
        print(min(arr))
        print(max(arr))
        print(median_value(arr))


print_statistics([])