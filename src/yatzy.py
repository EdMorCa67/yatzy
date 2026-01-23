class Yatzy:

    # Class propierties
    PIPS = {
        'ONE' : 1,
        'TWO' : 2,
        'THREE' : 3,
        'FOUR' : 4,
        'FIVE' : 5,
        'SIX' : 6,
    }
    ZERO = 0
    FIFTY = 50


    @staticmethod
    # A parameter list has too many parameters 
    # Code is duplicated
    def chance_scores_sum_of_all_dice(*dice):
        return sum(dice)

    @classmethod
    # A primitive data type is overloaded
    
    def yatzy(cls, dice):
        first = dice[0]
        for die in dice:
            if die != first:
                return cls.ZERO
        return cls.FIFTY
    

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_ones(cls, *dice):
        ONE = cls.PIPS['ONE']
        return sum([ONE for die in dice if die == ONE])


    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_twos(cls, *dice):
        TWO = cls.PIPS['TWO']
        return sum([TWO for die in dice if die == TWO])
         

    @classmethod
    # A parameter list has too many parameters
    # Code is duplicated
    # A variable has a poor name
    def sum_threes(cls, *dice):
        THREE = cls.PIPS['THREE']
        return sum([THREE for die in dice if die == THREE])

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_fours(cls, *dice):
        FOUR = cls.PIPS['FOUR']
        return sum([FOUR for die in dice if die == FOUR])

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_fives(cls, *dice):
        FIVE = cls.PIPS['FIVE']
        return sum([FIVE for die in dice if die == FIVE])

    @classmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_sixes(cls, *dice):
        SIX = cls.PIPS['SIX']
        return sum([SIX for die in dice if die == SIX])
    

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
    def score_two_pair(cls, *dice):
        PAIR = 2
        pair_pip = list(die for die in sorted(dice) if dice.count(die) >= PAIR)
        if len(set(pair_pip)) == 2:
            return sum(set(pair_pip)) * PAIR
        else:
           return cls.ZERO

    @staticmethod
    def score_three_of_a_kind(*dice):
        THREE_OF_A_KIND = 3
        three_of_a_kind_pip = list(die for die in sorted(dice) if dice.count(die) >= THREE_OF_A_KIND)
        if three_of_a_kind_pip != []:
            return  max(three_of_a_kind_pip) * THREE_OF_A_KIND
        return 0

    @classmethod
    def score_four_of_a_kind(cls, *dice):
        FOUR_OF_A_KIND = 4
        four_of_a_kind_pip = list(die for die in sorted(dice) if dice.count(die) >= FOUR_OF_A_KIND)
        if four_of_a_kind_pip != []:
            return  max(four_of_a_kind_pip) * FOUR_OF_A_KIND
        return cls.ZERO

    @classmethod
    def score_straight(cls, *dice):
        SMALL_STRAIGHT = set(list(cls.PIPS.values())) - {cls.PIPS['SIX']}
        LARGE_STRAIGHT = set(list(cls.PIPS.values())) - {cls.PIPS['ONE']}
        tidy_dices = set(dice)
        if tidy_dices == SMALL_STRAIGHT or tidy_dices == LARGE_STRAIGHT:
            return sum(dice)
        return cls.ZERO

    @classmethod
    def score_full_house(cls, *dice):
        MAX_DISSTINCT_VALUES = 2
        return sum(dice) if len(set(dice)) == MAX_DISSTINCT_VALUES else cls.ZERO