from src.pips import Pips
from src.combinations import Combinations


class Yatzy:
    # Class propierties

    ZERO = 0
    FIFTY = 50

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def chance(*dice):
        return sum(dice)

    @classmethod
    # A primitive data type is overloaded
    def yatzy(cls, dice):
        ALL_THE_SAME = Combinations.ALL_THE_SAME.value
        return (
            cls.FIFTY 
            if len(set(dice)) == ALL_THE_SAME 
            else cls.ZERO
        )
    
    @staticmethod
    def __sum_dice_score(dice, pip):
        return sum(filter(lambda die: die == pip, dice))

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def ones(cls, *dice):
        PIP = Pips.ONE.value
        return cls.__sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def twos(cls, *dice):
        PIP = Pips.TWO.value
        return cls.__sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    # A variable has a poor name
    def threes(cls, *dice):
        PIP = Pips.THREE.value
        return cls.__sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def fours(cls, *dice):
        PIP = Pips.FOUR.value
        return cls.__sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def fives(cls, *dice):
        PIP = Pips.FIVE.value
        return cls.__sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sixes(cls, *dice):
        PIP = Pips.SIX.value
        return cls.__sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def score_pair(cls, *dice):
        PAIR = Combinations.PAIR.value
        pip_pair = [die for die in sorted(dice) if dice.count(die) >= PAIR]
        return (
            max(pip_pair) * PAIR 
            if pip_pair 
            else cls.ZERO
        )

    @classmethod
    def two_pair(cls, *dice):
        TWO_PAIR = Combinations.TWO_PAIR.value
        pip_pairs = set([die for die in sorted(dice) if dice.count(die) >= TWO_PAIR])
        return (
            cls.chance(*pip_pairs) * TWO_PAIR
            if len(pip_pairs) == TWO_PAIR
            else cls.ZERO
        )

    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE_OF_A_KIND = Combinations.THREE_OF_A_KIND.value
        three_of_a_kind_pip = [
            die for die in sorted(dice) if dice.count(die) >= THREE_OF_A_KIND
        ]
        return (
            max(three_of_a_kind_pip) * THREE_OF_A_KIND
            if three_of_a_kind_pip
            else cls.ZERO
        )

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR_OF_A_KIND = Combinations.FOUR_OF_A_KIND.value
        four_of_a_kind_pip = [
            die for die in sorted(dice) if dice.count(die) >= FOUR_OF_A_KIND
        ]
        return (
            max(four_of_a_kind_pip) * FOUR_OF_A_KIND 
            if four_of_a_kind_pip 
            else cls.ZERO
        )

    @classmethod
    def smallStraight(cls, *dice):
        SMALL_STRAIGHT = Pips.minus(Pips.SIX)
        tidy_dices = set(dice)
        return (
            cls.chance(*dice) 
            if tidy_dices == SMALL_STRAIGHT 
            else cls.ZERO
        )

    @classmethod
    def largeStraight(cls, *dice):
        LARGE_STRAIGHT = Pips.minus(Pips.ONE)
        tidy_dices = set(dice)
        return (
            cls.chance(*dice) 
            if tidy_dices == LARGE_STRAIGHT 
            else cls.ZERO
        )

    @classmethod
    def fullHouse(cls, *dice):
        MAX_DISTINCT_VALUES = Combinations.FULL_HOUSE_DIFERENT_VALUES.value
        return (
            cls.chance(*dice) 
            if len(set(dice)) == MAX_DISTINCT_VALUES 
            else cls.ZERO
        )
