"""
Дана довільна строка.
Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
"""
eng_vowels = 'aeiou'

text = 'Foaog evearywheree. Aim up the river, where it flows aamoaaangaa gaaareenaaa its and meadows;'
lower_text = text.lower()
text_to_list = lower_text.split()

result_words = []

for word in text_to_list:
    letters_counter = 0
    for letter in word:
        if letter in eng_vowels:
            letters_counter += 1
        else:
            letters_counter = 0
        if letters_counter > 2:
            result_words.remove(word)
        if letters_counter == 2:
            result_words.append(word)

result_words_set = set(result_words)
# print(result_words_set)
print(f'The number of words that contain 2 vowels in a row: {len(result_words_set)}')

# Будь ласка, прочитайте пояснення до коду
"""
У задачі сказано, що повинні враховуватися слова, в яких 2 голосні поспіль, але не більше. 
Для цього було додано умову, що якщо в слові більше 2 голосних – виключати його зі списку.
У такому разі доводиться перебирати кожне слово до кінця і якщо в слові 2 рази збігається умова завдання - 
то слово дублюється до списку. Тому додано змінну, в якій список перетворений на set() 
і в ньому вже рахується кількість слів, що потрапляють під умову.

Якщо умова передбачає щонайменше 2 голосні поспіль - тоді після умови 
' if letters_counter == 2:
    result_words.append(word)' 
    стояв би 
    break, 
що дозволило б уникнути повторень слів у списку і не потрібно було робити перетворення списку в set().
"""

