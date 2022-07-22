import pytest
from Homework_10.homework_10_funcs import apply_to_collection_items

def divide_item(arg: int) -> float:
    return arg / 2

def divide_item_wrong_arg_num(arg: int, a) -> float:
    return arg / 2 + a

@pytest.mark.parametrize('collection, expected_result', [([2, 4, 6, 8], [1.0, 2.0, 3.0, 4.0])])
def test_apply_to_collection_items(collection, expected_result):
    assert apply_to_collection_items(divide_item, collection) == expected_result

@pytest.mark.parametrize('collection', [([2, 4, 6, 8])])
def test_apply_to_collection_items_incorrect_args_number(collection):
    with pytest.raises(ValueError, match='Invalid function argument\'s number'):
        apply_to_collection_items(divide_item_wrong_arg_num, collection)

@pytest.mark.parametrize('collection', [([2, 4, 6, 8, '2'])])
def test_apply_to_collection_items_incorrect_args_type(collection):
    with pytest.raises(ValueError, match='Function\'s argument and collection item type mismatch'):
        apply_to_collection_items(divide_item, collection)

