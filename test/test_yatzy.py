from src.yatzy import Yatzy
import pytest

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy.scores_sum_of_all_dice(2, 3, 4, 5, 1)
    assert expected == actual
    assert 16 == Yatzy.scores_sum_of_all_dice(3, 3, 4, 5, 1)

@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([4, 4, 4, 4, 4], 50),
        ([6, 6, 6, 6, 6], 50),
        ([6, 6, 6, 6, 3], 0)
    ],
)
def test_yatzy_scores_fifty(dices, expected_result):
    assert Yatzy.yatzy(dices) == expected_result


def test_sum_ones():
    assert Yatzy.ones(1, 2, 3, 4, 5) == 1
    assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
    assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
    assert 4 == Yatzy.ones(1, 2, 1, 1, 1)


def test_sum_twos():
    assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
    assert 10 == Yatzy.twos(2, 2, 2, 2, 2)


def test_sum_threes():
    assert 6 == Yatzy.threes(1, 2, 3, 2, 3)
    assert 12 == Yatzy.threes(2, 3, 3, 3, 3)


def test_sum_fours():
    assert 12 == Yatzy(4, 4, 4, 5, 5).fours()
    assert 8 == Yatzy(4, 4, 5, 5, 5).fours()
    assert 4 == Yatzy(4, 5, 5, 5, 5).fours()


def test_sum_fives():
    assert 10 == Yatzy(4, 4, 4, 5, 5).fives()
    assert 15 == Yatzy(4, 4, 5, 5, 5).fives()
    assert 20 == Yatzy(4, 5, 5, 5, 5).fives()


def test_sum_sixes():
    assert 0 == Yatzy(4, 4, 4, 5, 5).sixes()
    assert 6 == Yatzy(4, 4, 6, 5, 5).sixes()
    assert 18 == Yatzy(6, 5, 6, 6, 5).sixes()


def test_one_pair():
    assert 6 == Yatzy().score_pair(3, 4, 3, 5, 6)
    assert 10 == Yatzy().score_pair(5, 3, 3, 3, 5)
    assert 12 == Yatzy().score_pair(5, 3, 6, 6, 5)


def test_two_pair():
    assert 16 == Yatzy().two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy().two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy().two_pair(3, 3, 6, 5, 4)


def test_three_of_a_kind():
    assert 9 == Yatzy().three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy().three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)


def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)


def test_small_straight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy().smallStraight(1, 2, 2, 4, 5)


def test_large_straight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy().largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_full_house():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)