check = False


def polite_input(question):
    global check
    if check == False:
        global name
        name = input('Как вас зовут?')
        check = True
    else:
        pass
    optional = '{}, {}'.format(name, question)
    answer = input(optional)


age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')