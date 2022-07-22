from datetime import date
import pytest

from Homework_9.homework_9_human_class import Human

@pytest.fixture
def human():
    return Human('Leia', 'Skywalker-Organa-Solo', 'w', birth_date=date(1977, 10, 27))

@pytest.mark.parametrize('dish_name, expected_result', [('snacks', 'Leia\'s favourite dish is snacks')])
def test_eat(capsys, human, dish_name, expected_result):
    human.eat(dish_name)
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('sleeping_hours, expected_result', [(8.5, 'Leia usually sleeps 8.5 hours')])
def test_sleep(capsys, human, sleeping_hours, expected_result):
    human.sleep(sleeping_hours)
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('expected_result', ['Leia sometimes talking to herself'])
def test_talk(capsys, human, expected_result):
    human.talk()
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('expected_result', ['Leia prefers walking instead of taking the subway or taxi'])
def test_walk(capsys, human, expected_result):
    human.walk()
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('expected_result', ['Leia has a high desk at home so Leia can work standing up.'])
def test_stand(capsys, human, expected_result):
    human.stand()
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('expected_result', ['Leia used to read books lying down'])
def test_lie(capsys, human, expected_result):
    human.lie()
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('expected_result', [44])
def test_counts_age(human, expected_result):
    assert human.counts_age == expected_result


