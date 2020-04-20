under_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
big_num = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def number_in_english(num):
    if len(str(num)) == 1:
        return under_20[num]
    elif len(str(num)) == 2:
        if num < 20:
            return under_20[num]
        if num >= 20:
            if num % 10 == 0:
                return big_num[num // 10]
            else:
                return '{} {}'.format(big_num[num // 10], under_20[num % 10])
    elif len(str(num)) == 3:
        if num % 100 == 0:
            return '{} hundred'.format(under_20[num // 100])
        elif ((num % 100) < 20) and (num % 100 != 0):
            return '{} hundred and {}'.format(under_20[num // 100],  under_20[num % 100])
        elif (num % 100) >= 20 and str(num)[-1] == '0':
            return '{} hundred and {}'.format(under_20[num // 100], big_num[(num % 100) // 10])
        elif (num % 100) >= 20 and str(num)[-1] != '0':
            return '{} hundred and {} {}'.format(under_20[num // 100], big_num[(num % 100) // 10], under_20[(num % 100) % 10])


print(number_in_english(0).lower())