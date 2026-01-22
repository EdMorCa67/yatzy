class Yatzy:
    ZERO = 0
    FIFTY = 50


    @staticmethod
    # A parameter list has too many parameters 
    # Code is duplicated
    def chance_scores_sum_of_all_dice(*dice):
        return sum(dice)

    @staticmethod
    # A primitive data type is overloaded
    
    def yatzy(dice):
        first = dice[0]
        for die in dice:
            if die != first:
                return Yatzy.ZERO
        return Yatzy.FIFTY
    

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_ones(*dice):
        ONE = 1
        return sum([ONE for die in dice if die == ONE])


    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_twos(*dice):
        TWO = 2
        return sum([TWO for die in dice if die == TWO])
         

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    # A variable has a poor name
    def sum_threes(*dice):
        THREE = 3
        return sum([THREE for die in dice if die == THREE])

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_fours(*dice):
        FOUR = 4
        return sum([FOUR for die in dice if die == FOUR])

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_fives(*dice):
        FIVE = 5
        return sum([FIVE for die in dice if die == FIVE])

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_sixes(*dice):
        SIX = 6
        return sum([SIX for die in dice if die == SIX])
    

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def score_pair(*dice):
        PAIR = 2
        pair_pip = list(die for die in sorted(dice) if dice.count(die) >= PAIR)
        if pair_pip != []:
            return  max(pair_pip) * PAIR
        return Yatzy.ZERO

    @staticmethod
    def score_two_pair(*dice):
        PAIR = 2
        pair_pip = list(die for die in sorted(dice) if dice.count(die) >= PAIR)
        if len(set(pair_pip)) == 2:
            return sum(set(pair_pip)) * PAIR
        else:
           return Yatzy.ZERO

    @staticmethod
    def score_three_of_a_kind(*dice):
        THREE_OF_A_KIND = 3
        three_of_a_kind_pip = list(die for die in sorted(dice) if dice.count(die) >= THREE_OF_A_KIND)
        if three_of_a_kind_pip != []:
            return  max(three_of_a_kind_pip) * THREE_OF_A_KIND
        return 0

    @staticmethod
    def score_four_of_a_kind(*dice):
        FOUR_OF_A_KIND = 4
        four_of_a_kind_pip = list(die for die in sorted(dice) if dice.count(die) >= FOUR_OF_A_KIND)
        if four_of_a_kind_pip != []:
            return  max(four_of_a_kind_pip) * FOUR_OF_A_KIND
        return Yatzy.ZERO

    @staticmethod
    def score_straight(*dice):
        SMALL_STRAIGHT = [1, 2, 3, 4, 5]
        LARGE_STRAIGHT = [2, 3, 4, 5, 6]
        tidy_dices = sorted(dice)
        if tidy_dices == SMALL_STRAIGHT or tidy_dices == LARGE_STRAIGHT:
            return sum(dice)
        return Yatzy.ZERO

    @staticmethod
    def score_full_house(*dice):
        MAX_DISSTINCT_VALUES = 2
        return sum(dice) if len(set(dice)) == MAX_DISSTINCT_VALUES else Yatzy.ZERO