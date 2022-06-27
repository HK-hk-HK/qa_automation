"""
Є два довільних числа які відповідають за мінімальну і максимальну ціну.
Є Dict з назвами магазинів і цінами:
{ "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999,
"main-service": 37.245, "buy.ua": 38.324,
"my-store": 37.166, "the_partner": 38.988,
"sto": 37.720, "rozetka": 38.003}.
Напишіть код, який знайде і виведе на екран назви магазинів,
ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:
lower_limit = 35.9
upper_limit = 37.339
> match: "my-store", "main-service"
"""

lower_limit = 35.9
upper_limit = 38.988

shop_dict = {"cilpio": 47.999, "a_studio": 42.999, "momo": 49.999,
             "main-service": 37.245, "buy.ua": 38.324,
             "my-store": 37.166, "the_partner": 38.988,
             "sto": 37.720, "rozetka": 38.003}

matched_keys = []

for shop_key, shop_value in shop_dict.items():
    if lower_limit <= shop_value <= upper_limit:
        matched_keys.append(shop_key)

print(f'Match: {matched_keys}')