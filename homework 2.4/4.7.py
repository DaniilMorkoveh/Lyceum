import itertools


nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']
suit = ['Пик', 'Треф', 'Бубен', 'Червей']
suit.remove(input('Какую масть убрать? ').capitalize())
for card in itertools.product(nominal, suit):
    print(*card)