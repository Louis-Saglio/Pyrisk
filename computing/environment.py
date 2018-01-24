import random
import statistics

import gengine

import fight


class Environment(gengine.Environment):

    def __init__(self, nbr_defensors, nbr_remaining):
        self.nbr_remaining = nbr_remaining
        self.nbr_defensors = nbr_defensors

    def get_initial_chromosomes(self):
        # return randint(int(0.5 * self.nbr_defensors), int(1.5 * self.nbr_defensors))
        return random.randint(int(0.1 * self.nbr_defensors), int(5 * self.nbr_defensors))

    def get_grade(self, chromosomes) -> float:
        return abs(self.nbr_remaining - fight.fight_n(chromosomes, self.nbr_defensors, 100)[0])

    def mate(self, chromosome_1, chromosome_2):
        return round(statistics.mean((chromosome_1, chromosome_2)))

    def mutate(self, chromosomes):
        return random.randint(0, self.nbr_defensors * 2)
