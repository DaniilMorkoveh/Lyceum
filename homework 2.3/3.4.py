def weight_of_words(word):
    word = word.upper()
    summa = 0
    for letter in word:
        summa += (ord(letter) - ord('A') + 1)
    return summa


list_of_words = []
list_of_nums = []
gem = {}
while True:
    nw = input()
    if nw == "":
        break
    list_of_words.append(nw)


list_of_nums.append(weight_of_words(nw))
gem[weight_of_words(nw)] = []
for word in list_of_words:
    gem[weight_of_words(word)].append(word)
gem[weight_of_words(word)].sort()
list_of_nums.sort()
for num in list_of_nums:
    for l in range(len(gem[num])):
        print(gem[num][l])