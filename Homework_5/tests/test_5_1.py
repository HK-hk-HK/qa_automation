import pytest

from Homework_5.homework_5_1_task import print_type

# test positive scenarios
def test_print_type_positive(capsys):
    print_type(type(7))
    captured = capsys.readouterr()
    assert 'int' in captured.out
    print_type(type('test'))
    captured = capsys.readouterr()
    assert 'str' in captured.out
    print_type(type(1.1))
    captured = capsys.readouterr()
    assert 'float' in captured.out
    print_type(type([]))
    captured = capsys.readouterr()
    assert 'list' in captured.out

# test negative: if the function without argument
def test_print_type_negative(capsys):
    with pytest.raises(TypeError):
        print_type()

