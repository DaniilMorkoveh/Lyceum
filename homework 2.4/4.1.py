def group_cities(list_of_cities):
    dicity = {}
    population = []
    for city in list_of_cities:
        city = city.split()
    population.append(city[2])
    population.sort()
    ad_keys = []
    for pop in population:
        if (int(pop) // 100000 * 100) not in ad_keys:
            ad_keys.append(int(pop) // 100000 * 100)
        dicity[f'{int(pop) // 100000 * 100} - {(int(pop) // 100000 + 1) * 100}'] = []
    for city_ in city.split('\n'):
        city_ = city_.split()
        dicity[f'{int(city_[2]) // 100000 * 100} - {(int(city_[2]) // 100000 +1) * 100}'].append(city_[0])
    for k in sorted(ad_keys):
        ad = f'{k} - {k + 100}'
        print(f'{ad}: {", ".join(dicity[ad])}')


cities = '''Братислава Словакия 625167
Брюссель Бельгия 1154635
Будапешт Венгрия 1757618
Белград Сербия 1233796
Прага Чехия 1267449
София Болгария 1286383
Тбилиси Грузия 1118035'''
ncities = cities.split('\n')
group_cities(ncities)