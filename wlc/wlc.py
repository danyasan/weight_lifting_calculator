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

BARBELL = 45  # lbs


def weight_per_side(target: float) -> float:
    """
    Return how much weight to place on each side of the bar to reach the target
    weight.
    """
    if target < BARBELL:
        raise ValueError(
            f"The barbell weighs {BARBELL} lbs, "
            f"{BARBELL - target} lbs more than you're trying to lift!"
        )
    weight_one_side = (target - BARBELL) / 2
    return weight_one_side


def weight_being_lifted(weight_one_side: float) -> float:
    """
    Calculate the total weight being lifted from the sum of weights on
    one side of the bar.
    """
    return weight_one_side * 2 + BARBELL


def solve_weight_per_side(side_weight: float) -> list[tuple[float]]:
    """
    Given the target plate weight (mass on one side of the barbell) and the
    weight collection, WEIGHT, return a list of tuples containing the plate
    weights from the collection that will result in the desired weight.

    For example, to hit 45 lbs, the following combinations of plate weights
    could be used:
    * (45, )
    * (35, 10)
    * (25, 10, 10)
    * etc.
    """
    solutions = []
    for n in range(len(WEIGHTS) + 1):
        combos = combinations(WEIGHTS, n)
        for i in list(combos):
            if sum(i) == side_weight and i not in solutions:
                solutions.append(i)
    return solutions


def solve_weight_per_side_fuzzy(side_weight: float) -> list[tuple[float]]:
    """
    If no solution is found, try looking slightly above or below the target to
    find a solution.
    """
    # TODO implement some way of letting user know this got rounded.
    rounded_weight = round_to_5(side_weight)
    solutions = solve_weight_per_side(rounded_weight)

    if not solutions:
        raise ValueError(
            f"Can't make {side_weight} lbs on each side with "
            f"current plate collection!"
        )
    return solutions


def weights_for_target(target: float) -> list[tuple[float]]:
    """
    Given a target mass to lift, return the available weight combinations
    to put on one side of the bar to reach that target mass.

    For example, to lift 135 lbs total with a 45 lbs barbell, 45 lbs should
    be used on each side. This function will return the different plate
    combinations to use, limited to plates from the weight collection.
    """
    side_weight = weight_per_side(target)
    solutions = solve_weight_per_side(side_weight)
    if not solutions:
        solutions = solve_weight_per_side_fuzzy(side_weight)
    return solutions


def round_to_5(mass: float) -> float:
    remainder = mass % 5
    if remainder == 0:
        return mass
    elif remainder < 2.5:
        return mass - remainder
    elif remainder >= 2.5:
        return mass + (5 - remainder)


def find_warmup_weights(target: float) -> list[float]:
    """
    Given the target mass to lift, return a list of plate combinations
    to work through up to the target mass. First set is the empty barbell.
    Does not include the target mass.

    Assumes the warm-ups consist of:
    3 sets of 5
    1 set of 5
    1 set of 3
    1 set of 1
    3 sets of 5 (work set; excluded)
    """
    delta = target - BARBELL
    spacing = delta / 4
    return [
        BARBELL,
        round_to_5(BARBELL + spacing),
        round_to_5(BARBELL + 2 * spacing),
        round_to_5(BARBELL + 3 * spacing),
    ]


def get_full_workout_solution(target: float) -> list[tuple[float]]:
    """
    Given a target mass, return which plates to put on each side of the barbell
    for each warmup set and the work set.

    For simplicity, just provides the first solution for each warmup set.
    """
    workout = find_warmup_weights(target)
    workout.append(target)
    workout_combos = [weights_for_target(mass)[0] for mass in workout]
    return workout_combos
