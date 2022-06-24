"""
Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
Слово та номер отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
"""
# 1 task with one input; all elements and their order are printed

word2 = input('Input some word: ')

if word2 == '':
    print('"Word field" can\'be empty')
else:
    for elem in range(len(word2)):
        order = elem + 1
        print(f'The {order} symbol  in "{word2}" is "{word2[elem]}"')

