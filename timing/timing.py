import random
import helpers


@helpers.parallel
@helpers.chrono(100000)
def get_dice_result(dice_number, mini=1, maxi=6):
    assert isinstance(dice_number, int)
    assert isinstance(mini, int)
    assert isinstance(mini, int)
    assert 0 < mini < maxi
    assert dice_number > 1
    """
    return a list of {dice_number} random int between {mini} and {maxi} included, sorted by value, greatest last.
    """
    return sorted({random.randint(mini, maxi) for _ in range(dice_number)})


@helpers.parallel
@helpers.chrono(100000)
def get_dice_result_4(dice_number, mini=1, maxi=6):
    """
    return a list of {dice_number} random int between {mini} and {maxi} included, sorted by value, greatest last.
    """
    return sorted({random.randint(mini, maxi) for _ in range(dice_number)})


@helpers.parallel
@helpers.chrono(100000)
def get_dice_result_2(dice_number, mini=1, maxi=6):
    return sorted((random.randint(mini, maxi) for _ in range(dice_number)), reverse=True)


@helpers.parallel
@helpers.chrono(100000)
def get_dice_result_3(dice_number, mini=1, maxi=6):
    data = [random.randint(mini, maxi) for _ in range(dice_number)]
    data.sort()
    return data


rn = 1_000
rn2 = 9_000


@helpers.parallel
@helpers.chrono(rn)
def random_number():
    g = (random.randint(1, 6) for _ in range(rn2))
    for i in g:
        a = i


@helpers.parallel
@helpers.chrono(rn)
def random_number_2():
    g = {random.randint(1, 6) for _ in range(rn2)}
    for i in g:
        a = i


@helpers.parallel
@helpers.chrono(rn)
def random_number_3():
    g = [random.randint(1, 6) for _ in range(rn2)]
    for i in g:
        a = i


@helpers.parallel
@helpers.chrono(rn)
def make_tuple():
    return 1, 2, 3, 4, 5


@helpers.parallel
@helpers.chrono(rn)
def make_list():
    return [1, 2, 3, 4, 5]


get_dice_result(10)
get_dice_result_4(10)
get_dice_result_2(10)
get_dice_result_3(10)
random_number()
random_number_2()
random_number_3()

make_tuple()
make_list()
