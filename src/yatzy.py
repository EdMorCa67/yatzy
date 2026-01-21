class Yatzy:

    @staticmethod
    # A parameter list has too many parameters 
    # Code is duplicated
    def chance_scores_sum_of_all_dice(*dices):
        score = sum(dices)
        return score

    @staticmethod
    # A primitive data type is overloaded
    
    def yatzy(dices):
        first = dices[0]
        for dice in dices:
            if dice != first:
                return 0
        return 50
    

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_ones(*dices):
        ONE = 1
        ones = sum([ONE for dice in dices if dice == ONE])
        return ones

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    def sum_twos(*dices):
        TWO = 2
        twos = sum([TWO for dice in dices if dice == TWO])
        return twos

    @staticmethod
    # A parameter list has too many parameters
    # Code is duplicated
    # A variable has a poor name
    def sum_threes(*dices):
        THREE = 3
        threes = sum([THREE for dice in dices if dice == THREE])
        return threes

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Cambia de método
    def sum_fours(*dices):
        FOUR = 4
        fours = sum([FOUR for dice in dices if dice == FOUR])
        return fours

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Cambia de método
    def sum_fives(*dices):
        FIVE = 5
        fives = sum([FIVE for dice in dices if dice == FIVE])
        return fives

    @staticmethod
    # A parameter list has too many parameters
    # A variable has a poor name
    # Cambia de método
    def sum_sixes(*dices):
        SIX = 6
        sixes = sum([SIX for dice in dices if dice == SIX])
        return sixes

    def score_pair(self, d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0