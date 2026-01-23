from src.pips import Pips

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
        ALL_THE_SAME = 1
        if len(set(dice)) == ALL_THE_SAME:
            return cls.FIFTY
        return cls.ZERO
    

    @staticmethod
    def sum_dice_score(dice, pip):
        return sum([pip for die in dice if die == pip])
    

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def ones(cls, *dice):
        PIP = Pips.ONE.value
        return cls.sum_dice_score(dice, PIP)


    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def twos(cls, *dice):
        PIP = Pips.TWO.value
        return cls.sum_dice_score(dice, PIP)
         

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    # A variable has a poor name
    def threes(cls, *dice):
        PIP = Pips.THREE.value
        return cls.sum_dice_score(dice, PIP)


    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def fours(cls, *dice):
        PIP = Pips.FOUR.value
        return cls.sum_dice_score(dice, PIP)


    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def fives(cls, *dice):
        PIP = Pips.FIVE.value
        return cls.sum_dice_score(dice, PIP)

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sixes(cls, *dice):
        PIP = Pips.SIX.value
        return cls.sum_dice_score(dice, PIP)
    

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def score_pair(cls, *dice):
        PAIR = 2
        pair_pip = list(die for die in sorted(dice) if dice.count(die) >= PAIR)
        if pair_pip != []:
            return  max(pair_pip) * PAIR
        return cls.ZERO


    @classmethod
    def two_pair(cls, *dice):
        PAIR = 2
        pair_pip = list(die for die in sorted(dice) if dice.count(die) >= PAIR)
        if len(set(pair_pip)) == 2:
            return sum(set(pair_pip)) * PAIR
        else:
           return cls.ZERO


    @classmethod
    def three_of_a_kind(cls, *dice):
        THREE_OF_A_KIND = 3
        three_of_a_kind_pip = list(die for die in sorted(dice) if dice.count(die) >= THREE_OF_A_KIND)
        if three_of_a_kind_pip != []:
            return  max(three_of_a_kind_pip) * THREE_OF_A_KIND
        return cls.ZERO


    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR_OF_A_KIND = 4
        four_of_a_kind_pip = list(die for die in sorted(dice) if dice.count(die) >= FOUR_OF_A_KIND)
        if four_of_a_kind_pip != []:
            return  max(four_of_a_kind_pip) * FOUR_OF_A_KIND
        return cls.ZERO
    
    
    @classmethod
    def smallStraight(cls, *dice):
        SMALL_STRAIGHT = Pips.minus(Pips.SIX)
        tidy_dices = set(dice)
        if tidy_dices == SMALL_STRAIGHT:
            return cls.chance(*dice)
        return cls.ZERO
    

    @classmethod
    def largeStraight(cls, *dice):
        LARGE_STRAIGHT = Pips.minus(Pips.ONE)
        tidy_dices = set(dice)
        if tidy_dices == LARGE_STRAIGHT:
            return cls.chance(*dice)
        return cls.ZERO
    

    @classmethod
    def fullHouse(cls, *dice):
        MAX_DISTINCT_VALUES = 2
        return sum(dice) if len(set(dice)) == MAX_DISTINCT_VALUES else cls.ZERO