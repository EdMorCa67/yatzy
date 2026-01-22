class Yatzy:
    ZERO = 0
    FIFTY = 50


    @staticmethod
    # A parameter list has too many parameters 
    # Code is duplicated
    def chance_scores_sum_of_all_dice(*dices):
        return sum(dices)

    @staticmethod
    # A primitive data type is overloaded
    
    def yatzy(dices):
        first = dices[0]
        for dice in dices:
            if dice != first:
                return Yatzy.ZERO
        return Yatzy.FIFTY
    

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_ones(*dices):
        ONE = 1
        return sum([ONE for dice in dices if dice == ONE])


    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_twos(*dices):
        TWO = 2
        return sum([TWO for dice in dices if dice == TWO])
         

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    # A variable has a poor name
    def sum_threes(*dices):
        THREE = 3
        return sum([THREE for dice in dices if dice == THREE])

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_fours(*dices):
        FOUR = 4
        return sum([FOUR for dice in dices if dice == FOUR])

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_fives(*dices):
        FIVE = 5
        return sum([FIVE for dice in dices if dice == FIVE])

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Change method
    def sum_sixes(*dices):
        SIX = 6
        return sum([SIX for dice in dices if dice == SIX])
    

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def score_pair(*dices):
        PAIR = 2
        pair_pip = list(dice for dice in sorted(dices) if dices.count(dice) >= PAIR)
        if pair_pip != []:
            return  max(pair_pip) * PAIR
        return Yatzy.ZERO

    @staticmethod
    def score_two_pair(*dices):
        PAIR = 2
        pair_pip = list(dice for dice in sorted(dices) if dices.count(dice) >= PAIR)
        if len(set(pair_pip)) == 2:
            return sum(set(pair_pip)) * PAIR
        else:
           return Yatzy.ZERO

    @staticmethod
    def score_three_of_a_kind(*dices):
        THREE_OF_A_KIND = 3
        three_of_a_kind_pip = list(dice for dice in sorted(dices) if dices.count(dice) >= THREE_OF_A_KIND)
        if three_of_a_kind_pip != []:
            return  max(three_of_a_kind_pip) * THREE_OF_A_KIND
        return 0

    @staticmethod
    def score_four_of_a_kind(*dices):
        FOUR_OF_A_KIND = 4
        four_of_a_kind_pip = list(dice for dice in sorted(dices) if dices.count(dice) >= FOUR_OF_A_KIND)
        if four_of_a_kind_pip != []:
            return  max(four_of_a_kind_pip) * FOUR_OF_A_KIND
        return Yatzy.ZERO

    @staticmethod
    def score_straight(*dices):
        SMALL_STRAIGHT = [1, 2, 3, 4, 5]
        LARGE_STRAIGHT = [2, 3, 4, 5, 6]
        tidy_dices = sorted(dices)
        if tidy_dices == SMALL_STRAIGHT or tidy_dices == LARGE_STRAIGHT:
            return sum(dices)
        return Yatzy.ZERO

    @staticmethod
    def score_full_house(*dices):
        MAX_DISSTINCT_VALUES = 2
        return sum(dices) if len(set(dices)) == MAX_DISSTINCT_VALUES else Yatzy.ZERO