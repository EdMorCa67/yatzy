from src.yatzy import Yatzy
import pytest

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy.chance_scores_sum_of_all_dice(2, 3, 4, 5, 1)
    assert expected == actual
    assert 16 == Yatzy.chance_scores_sum_of_all_dice(3, 3, 4, 5, 1)

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


@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([1, 2, 1, 4, 5], 2),
        ([6, 2, 2, 4, 5], 0),
        ([1, 2, 1, 1, 1], 4)
    ],
)
def test_sum_ones(dices, expected_result):
    assert Yatzy.sum_ones(*dices) == expected_result



@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([1, 2, 3, 2, 6], 4),
        ([2, 2, 2, 2, 2], 10),
        ([1, 2, 1, 1, 1], 2)
    ],
)
def test_sum_twos(dices, expected_result):
    assert Yatzy.sum_twos(*dices) == expected_result




@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([1, 2, 3, 2, 3], 6),
        ([2, 3, 3, 3, 3], 12),
        ([1, 2, 1, 1, 1], 0)
    ],
)
def test_sum_threes(dices, expected_result):
    assert Yatzy.sum_threes(*dices) == expected_result


@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([4, 4, 5, 5, 5], 8),
        ([4, 4, 4, 5, 5], 12),
        ([4, 5, 5, 5, 5], 4)
    ],
)
def test_sum_fours(dices, expected_result):
    assert Yatzy.sum_fours(*dices) == expected_result

@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([4, 4, 3, 5, 5], 10),
        ([4, 4, 5, 5, 5], 15),
        ([4, 5, 5, 5, 5], 20)
    ],
)
def test_sum_fives(dices, expected_result):
    assert Yatzy.sum_fives(*dices) == expected_result



@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([4, 4, 4, 5, 5], 0),
        ([4, 4, 6, 5, 5], 6),
        ([6, 5, 6, 6, 5], 18)
    ],
)
def test_sum_sixes(dices, expected_result):
    assert Yatzy.sum_sixes(*dices) == expected_result


@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([3, 4, 3, 5, 6], 6),
        ([4, 4, 6, 5, 5], 10),
        ([1, 5, 6, 6, 5], 12),
        ([1, 2, 3, 4, 5], 0)
    ],
)
def test_score_pair(dices, expected_result):
    assert Yatzy.score_pair(*dices) == expected_result


@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([3, 3, 5, 4, 5], 16),
        ([4, 4, 6, 5, 5], 18),
        ([3, 3, 6, 5, 4], 0),
        ([3, 3, 3, 3, 5], 0)
    ],
)
def test_score_two_pair(dices, expected_result):
    assert Yatzy.score_two_pair(*dices) == expected_result


@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([3, 3, 3, 4, 5], 9),
        ([5, 3, 5, 4, 5], 15),
        ([3, 3, 6, 5, 4], 0)
    ],
)
def test_score_three_of_a_kind(dices, expected_result):
    assert Yatzy.score_three_of_a_kind(*dices) == expected_result

@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([3, 3, 3, 3, 5], 12),
        ([5, 5, 5, 4, 5], 20),
        ([3, 3, 6, 5, 4], 0)
    ],
)
def test_score_four_of_a_kind(dices, expected_result):
    assert Yatzy.score_four_of_a_kind(*dices) == expected_result


@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([1, 2, 3, 4, 5], 15),
        ([2, 3, 4, 5, 1], 15),
        ([3, 3, 6, 5, 4], 0),
        ([6, 2, 3, 4, 5], 20),
        ([2, 3, 4, 5, 6], 20),
        ([3, 3, 6, 5, 1], 0)
    ],
)
def test_score_straight(dices, expected_result):
    assert Yatzy.score_straight(*dices) == expected_result

@pytest.mark.parametrize(
    "dices, expected_result",
    [
        ([6, 2, 2, 2, 6], 18),
        ([2, 3, 4, 5, 6], 0),
        ([1, 1, 5, 5, 5], 17)
    ],
)
def test_score_full_house(dices, expected_result):
    assert Yatzy.score_full_house(*dices) == expected_result

