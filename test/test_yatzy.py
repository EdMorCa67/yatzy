from src.yatzy import Yatzy
import pytest

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([2, 3, 4, 5, 1], 15),
        ([3, 3, 4, 5, 1], 16),
    ],
)

def test_chance_scores_sum_of_all_dice(dice, expected_result):
    assert Yatzy.chance(*dice) == expected_result 


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([4, 4, 4, 4, 4], 50),
        ([6, 6, 6, 6, 6], 50),
        ([6, 6, 6, 6, 3], 0)
    ],
)
def test_yatzy_scores_fifty(dice, expected_result):
    assert Yatzy.yatzy(dice) == expected_result


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([1, 2, 1, 4, 5], 2),
        ([6, 2, 2, 4, 5], 0),
        ([1, 2, 1, 1, 1], 4)
    ],
)
def test_sum_ones(dice, expected_result):
    assert Yatzy.ones(*dice) == expected_result



@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([1, 2, 3, 2, 6], 4),
        ([2, 2, 2, 2, 2], 10),
        ([1, 2, 1, 1, 1], 2)
    ],
)
def test_sum_twos(dice, expected_result):
    assert Yatzy.twos(*dice) == expected_result




@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([1, 2, 3, 2, 3], 6),
        ([2, 3, 3, 3, 3], 12),
        ([1, 2, 1, 1, 1], 0)
    ],
)
def test_sum_threes(dice, expected_result):
    assert Yatzy.threes(*dice) == expected_result


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([4, 4, 5, 5, 5], 8),
        ([4, 4, 4, 5, 5], 12),
        ([4, 5, 5, 5, 5], 4)
    ],
)
def test_sum_fours(dice, expected_result):
    assert Yatzy.fours(*dice) == expected_result

@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([4, 4, 3, 5, 5], 10),
        ([4, 4, 5, 5, 5], 15),
        ([4, 5, 5, 5, 5], 20)
    ],
)
def test_sum_fives(dice, expected_result):
    assert Yatzy.fives(*dice) == expected_result



@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([4, 4, 4, 5, 5], 0),
        ([4, 4, 6, 5, 5], 6),
        ([6, 5, 6, 6, 5], 18)
    ],
)
def test_sum_sixes(dice, expected_result):
    assert Yatzy.sixes(*dice) == expected_result


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([3, 4, 3, 5, 6], 6),
        ([4, 4, 6, 5, 5], 10),
        ([1, 5, 6, 6, 5], 12),
        ([1, 2, 3, 4, 5], 0)
    ],
)
def test_score_pair(dice, expected_result):
    assert Yatzy.score_pair(*dice) == expected_result


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([3, 3, 5, 4, 5], 16),
        ([4, 4, 6, 5, 5], 18),
        ([3, 3, 6, 5, 4], 0),
        ([3, 3, 3, 3, 5], 0)
    ],
)
def test_score_two_pair(dice, expected_result):
    assert Yatzy.two_pair(*dice) == expected_result


@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([3, 3, 3, 4, 5], 9),
        ([5, 3, 5, 4, 5], 15),
        ([3, 3, 6, 5, 4], 0)
    ],
)
def test_score_three_of_a_kind(dice, expected_result):
    assert Yatzy.three_of_a_kind(*dice) == expected_result

@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([3, 3, 3, 3, 5], 12),
        ([5, 5, 5, 4, 5], 20),
        ([3, 3, 6, 5, 4], 0)
    ],
)
def test_score_four_of_a_kind(dice, expected_result):
    assert Yatzy.four_of_a_kind(*dice) == expected_result

@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([1, 2, 3, 4, 5], 15),
        ([2, 3, 4, 5, 1], 15),
        ([3, 3, 6, 5, 4], 0),
    ],
)

def test_score_small_straight(dice, expected_result):
    assert Yatzy.smallStraight(*dice) == expected_result

@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([6, 2, 3, 4, 5], 20),
        ([2, 3, 4, 5, 6], 20),
        ([3, 3, 6, 5, 1], 0)
    ],
)
def test_score_large_straight(dice, expected_result):
    assert Yatzy.largeStraight(*dice) == expected_result



@pytest.mark.parametrize(
    "dice, expected_result",
    [
        ([6, 2, 2, 2, 6], 18),
        ([2, 3, 4, 5, 6], 0),
        ([1, 1, 5, 5, 5], 17)
    ],
)
def test_score_full_house(dice, expected_result):
    assert Yatzy.fullHouse(*dice) == expected_result

