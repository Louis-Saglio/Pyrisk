from helpers import chrono, parallel
import random


def get_dice_result(dice_number, mini=1, maxi=6):
    """
    return a list of {dice_number} random int between {mini} and {maxi} included, sorted by value, smallest first.
    """
    data = [random.randint(mini, maxi) for _ in range(dice_number)]
    data.sort()
    return data


nbr = 50_000


@parallel
@chrono(nbr)
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


@parallel
@chrono(nbr)
def fight_2(nbr_a, nbr_d):
    while nbr_a > 1 and nbr_d > 0:

        if nbr_a > 3:
            dice_a = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
            dice_a.sort()
            dice_b = get_dice_result(nbr_d if dice_a[-1] + dice_a[-2] >= 8 else 1)
        else:
            if nbr_a == 3:
                dice_a = [random.randint(1, 6), random.randint(1, 6)]
                dice_a.sort()
            else:
                dice_a = random.randint(1, 6),
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


fight_2(20, 20)
fight(20, 20)
