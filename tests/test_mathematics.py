from src.pythontraining.mathematics import multiply, divide, round_up


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(4, 5) == 0.8


def test_round_up():
    assert round_up(2.4) == 3
