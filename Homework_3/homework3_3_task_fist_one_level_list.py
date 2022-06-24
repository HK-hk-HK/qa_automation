"""
Існує ліст з різними даними, наприклад
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
"""
# Third task with one-level list

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 5.6, '6.8', -100]
result_list = []

for elem in list1:
    if isinstance(elem, bool):
        continue
    try:
        float(elem)
        result_list.append(elem)
    except ValueError:
        continue
    except TypeError:
        continue

print(result_list)