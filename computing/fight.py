import random
import statistics
import multiprocessing as mp
import resource

from helpers import parallel, chrono


def get_dice_result(dice_number, mini=1, maxi=6):
    """
    return a list of {dice_number} random int between {mini} and {maxi} included, sorted by value, smallest first.
    """
    data = [random.randint(mini, maxi) for _ in range(dice_number)]
    data.sort()
    return data


def fight(nbr_a, nbr_d):
    while nbr_a > 1 and nbr_d > 0:

        if nbr_a > 3:
            dice_a = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
            dice_a.sort()
            dice_b = get_dice_result(nbr_d if dice_a[-1] + dice_a[-2] >= 8 else 1)
        else:
            dice_a = get_dice_result(nbr_a - 1)
            try:
                dice_b = get_dice_result(nbr_d if dice_a[-1] + dice_a[-2] >= 8 else 1)
            except IndexError:
                dice_b = random.randint(1, 6),

        if dice_a[-1] > dice_b[-1]:
            nbr_a -= 1
        else:
            nbr_d -= 1

        try:
            if dice_a[-2] > dice_b[-2]:
                nbr_a -= 1
            else:
                nbr_d -= 1
        except IndexError:
            pass

    return nbr_a, nbr_d


@chrono(1)
def fight_n(nbr_a, nbr_d, nbr):
    sum_a, sum_d = [], []
    for _ in range(nbr):
        a, d = fight(nbr_a, nbr_d)
        sum_a.append(a)
        sum_d.append(d)
    return statistics.mean(sum_a), statistics.mean(sum_d)


@parallel
def a_fight(nbr_a, nbr_d, q):
    q.put(fight(nbr_a, nbr_d))


@chrono(1)
def a_fight_n(nbr_a, nbr_d, nbr):
    q = mp.Queue(nbr)
    for _ in range(nbr):
        a_fight(nbr_a, nbr_d, q)
    return statistics.mean(q.get()[0] for _ in range(nbr))


if __name__ == '__main__':
    print(resource.prlimit())
    print(a_fight_n(300, 100, 500))
    print(fight_n(300, 100, 500))
