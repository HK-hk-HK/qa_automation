import inspect
"""
Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент.
Певернути колекцію, кожен член якої є перетвореним членом вхідної колекції.

Нотатка. Обʼєкт функції, яку передаємо вказує на функцію, котра приймає один аргумент.
Не користуватися функціями map чи filter!!!
"""

def divide_item(arg: int) -> float:
    """
    Divides taken argument in type int by 2

    :param arg: argument in type int
    :return: divided by 2 argument in type float
    """
    return arg / 2

def apply_to_collection_items(func, my_collection: list[int]) -> list[float]:
    """
    Takes collection and '''divide_item()''' function with 1 argument
    and using the passed function, performs a division by 2 operation on each element of the collection

    :param func: func is taken as parameter that does division by 2
    :param my_collection: collection in type list that contains items in type int
    :return: collection in type list that contains divided by 2 items in type float
    """
    divided_items = []
    if len(inspect.signature(func).parameters) != 1:
        raise ValueError('Invalid function argument\'s number')
    for item in my_collection:
        item_type = type(item)
        arg_type = inspect.signature(func).parameters['arg'].annotation
        if item_type != arg_type:
            raise ValueError('Function\'s argument and collection item type mismatch')
        divided_items.append(func(item))
    return divided_items




