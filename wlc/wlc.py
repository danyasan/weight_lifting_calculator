from itertools import combinations


# Weights, in lbs. Put one value for each pair of weights.
WEIGHTS = [
    5,
    10,
    10,
    25,
    35,
    45,
]

BARBELL = 45 # lbs


def weight_per_side(target: int|float) -> int|float:
    """Return how mmuch weight to place on each side of the bar to reach the target weight."""
    if target < BARBELL:
        raise ValueError(f"The barbell weighs {BARBELL} lbs, more than you're trying to lift!")
    weight_one_side = (target - BARBELL)/2
    return weight_one_side


def weight_on_bar(weight_one_side: int|float) -> int|float:
    """Calculate the total weight being lifted from the sum of weights on one side of the bar."""
    return weight_one_side*2 + BARBELL


def solve_weights_for_side(target: int|float) -> list[tuple]:
    """
    Given the weight needed on each side of the barbell, `weight_one_side`, and
    the weight collection, return a list of tuples that will reach the desired weight.

    e.g., to hit target of 45 lbs, could be achieved with:
    * (45,)
    * (35, 10)
    * (25, 10, 10)
    * etc.
    """
    # if target < BARBELL:
    #     raise ValueError(f"The barbell ({BARBELL} lbs) weighs more than the target weight!")
    # if target == BARBELL:
    #     return [(0,)]
    solutions = []
    for n in range(len(WEIGHTS) + 1):
        combos = combinations(WEIGHTS, n)
        for i in list(combos):
            if sum(i) == target and i not in solutions:
                solutions.append(i)
    return solutions


# TODO continue refactoring here
def weights_for_target(target):
    """
    Given a target mass to lift, return the available weight combinations to get to that mass.
    """
    side = weight_per_side(target)
    solutions = solve_weights_for_side(side)
    if solutions:
        return solutions
    else:
        print(f"Can't make {side} lbs on each side with current weights!")


def find_warmups(workweight):
    """
    Given the workweight, return a list of relatively evenly spaced masses down to the barbell.

    Assumes the warm-ups consist of:
    3 sets of 5
    1 set of 5
    1 set of 3
    1 set of 1
    Workset: 3 sets of 5
    """
    diff = workweight - BARBELL
    # TODO make calcs round to nearest 5 or 10 for higher likelihood of finding a plate match.
    spacing = diff / 4
    warmups = [
        BARBELL,
        BARBELL + spacing,
        BARBELL + 2*spacing,
        BARBELL + 3*spacing,
        workweight
    ]
    return warmups


def workout_calculator(workweight):
    """
    Given a workweight, return which plates to put on each side for each warmup set and the workset.
    """
    warmup_weights = find_warmups(workweight)
    for warmup in warmup_weights:
        print(warmup)
        print(weights_for_target(warmup))
