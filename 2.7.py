def choose_coffee(preferences):
    global ingredients
    for elem in preferences:
        if elem == 'Эспрессо' and ingredients[0] > 0:
            ingredients[0] -= 1
            return 'Эспрессо'
        elif elem == 'Капучино' and ingredients[0] > 0 and ingredients[1] > 2:
            ingredients[0] -= 1
            ingredients[1] -= 3
            return 'Капучино'
        elif elem == 'Маккиато' and ingredients[0] > 1 and ingredients[1] > 0:
            ingredients[0] -= 2
            ingredients[1] -= 1
            return 'Маккиато'
        elif elem == 'Кофе по-венски' and ingredients[0] > 0 and ingredients[2] > 1:
            ingredients[0] -= 1
            ingredients[2] -= 2
            return 'Кофе по-венски'
        elif elem == 'Латте Маккиато' and ingredients[0] > 0 and ingredients[1] > 1 and ingredients[2] > 0:
            ingredients[0] -= 1
            ingredients[1] -= 2
            ingredients[2] -= 1
            return 'Латте Маккиато'
        elif elem == 'Кон Панна' and ingredients[0] > 0 and ingredients[2] > 0:
            ingredients[0] -= 1
            ingredients[2] -= 1
            return 'Кон Панна'
        else:
            return 'К сожалению, не можем предложить Вам напиток'


ingredients = [1, 2, 3]
print(choose_coffee('Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато, Кон Панна'.split(', ')))
print(choose_coffee('Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато, Кон Панна'.split(', ')))