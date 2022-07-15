"""
Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:

Попросіть користувача ввести свсвій вік.
- якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
- якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
- якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
- якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"

Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.

Наприклад :
"Тобі ж 5 років! Де твої батьки?"
"Вам 81 рік? Покажіть пенсійне посвідчення!"
"О, вам 33 роки! Який цікавий вік!"

Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг або тайпхінтінг.
Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.
P.S. Для цієї і для всіх наступних домашок пишіть в функціях докстрінги або хінтінг
"""


def transform_age_ending(age: str) -> str:
    """
    The function is created as helper for 'check_user_age' function. It's written to check ukrainian word 'рік'
    and then put it into the full sentence in right ending.
    Can be used independently

    :param age: Takes only one argument: str and it should be integer number. To use this function
                in right way ```input()``` should be passed as an argument. If user inputs wrong value then
                it will be validated and user will see a hint
    :return: The function checks inputted user age then returns ukrainian word 'рік' in relevant form
    """
    try:
        age_int = int(age)
        if age_int <= 0:
            return f'Вік користувача мае бути більше нуля'
        elif age_int > 99:
            return f'Вік користувача мае бути меньше 100'
        elif age_int in range(2, 5) or int(age[-1]) in range(2, 5) and age_int not in range(5, 19):
            return f'{age} роки'
        elif int(age[-1]) == 1 and age_int != 11:
            return f'{age} рік'
        else:
            return f'{age} років'
    except ValueError:
        return 'Введіть ціле число будь ласка (від 1 до 99)'


def check_user_age(age: str) -> str:
    """
    The function is created to check user's age and then to return right respond to the user, that depends on inputted
    number. Helper 'transform_age_ending' function is used inside this function to define right ending of the ukrainian
    word 'рік'

    :param age: Takes only one argument: str and it should be integer number. To use this function
                in right way ```input()``` should be passed as an argument. If user inputs wrong value then
                it will be validated and user will see a hint
    :return: The function returns the relevant cashier respond that depends on the inputted user age
    """
    try:
        age_int = int(age)
        age_ending = transform_age_ending(age)
        if age_int <= 0:
            return f'Вік користувача мае бути більше нуля'
        elif age_int > 99:
            return f'Вік користувача мае бути меньше 100'
        elif age_int < 7:
            return f'Тобі ж {age_ending}! Де твої батьки?'
        elif age.count(age[0]) == len(age) == 2:
            return f'О! Вам {age_ending}! Який цікавий вік!'
        elif age_int < 16:
            return f'Тобі лише {age_ending}, а це фільм для дорослих!'
        elif age_int > 65:
            return f'Вам {age_ending}? Покажіть пенсійне посвідчення'
        else:
            return f'Незважаючи на те, що вам {age_ending}, білетів всеодно нема!'
    except ValueError:
        return 'Введіть ціле число будь ласка (від 1 до 99)'



