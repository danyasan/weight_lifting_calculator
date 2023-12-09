import pytest

from wlc.wlc import (
    weight_per_side,
    weight_being_lifted, solve_weight_per_side, round_to_5)


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
    assert weight_being_lifted(45) == expected


def test_solve_weight_for_side_empty():
    expected = []
    assert solve_weight_per_side(1) == expected


def test_solve_weight_per_side_10():
    expected = [(10,)]
    assert solve_weight_per_side(10) == expected


def test_solve_weight_per_side_45():
    expected = [(45,), (10, 35), (10, 10, 25)]
    assert solve_weight_per_side(45) == expected


@pytest.mark.parametrize(
    "mass, expected",
    [
        (45, 45),
        (0, 0),
        (42.5, 45),
        (47.5, 50),
        (140, 140),
        (142, 140),
        (143, 145),
    ]
)
def test_round_to_5(mass, expected):
    assert round_to_5(mass) == expected
