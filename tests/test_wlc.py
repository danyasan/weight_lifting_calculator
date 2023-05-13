import pytest

from ..wlc.wlc import weight_per_side, weight_on_bar, solve_weights_for_side


@pytest.fixture
def barbell() -> int:
    return 45


@pytest.fixture
def weight_collection() -> list:
    return [45, 45, 25, 10, 5]


def test_weight_per_side():
    expected = 45
    assert weight_per_side(135) == expected


def test_weight_on_bar():
    expected = 135
    assert weight_on_bar(45) == expected


def test_solve_weights_for_side_empty():
    expected = []
    assert solve_weights_for_side(1) == expected


def test_solve_weights_for_side_zero():
    expected = [(0,)]
    assert solve_weights_for_side(BARBELL) == expected


def test_solve_weights_for_side_10():
    expected = [(10,), (5, 5)]
    assert solve_weights_for_side(10) == expected

