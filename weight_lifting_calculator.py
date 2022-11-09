"""Weight Lifting Calculator

Determine which weights to put on the bar to reach a certain total weight.

Uses a list of available weights in your home gym.
"""
# Weights, in lbs. Put one value for each pair of weights.
WEIGHTS = [
    5,
    10,
    10,
    25,
    35,
]

BARBELL = 15 # lbs


def weights_each_side(target):
    """Return a list of the weights to place on each side of the bar to reach the target weight."""
    if target % 5 != 0:
        print(f"Can't split {target} lbs evenly! Try a number divisible by 5.")
    elif target < BARBELL:
        print(f"The barbell weighs {BARBELL} lbs, more than you're trying to lift!")
    else:
        side = (target - BARBELL)/2
        return side

print(weights_each_side(135))
print(weights_each_side(137))
print(weights_each_side(30))


def weight_on_bar(total):
    """Calculate the total weight being lifted from the sum of weights on one side of the bar."""
    return total*2 + BARBELL

print(weight_on_bar(45))


from itertools import combinations

def weights_for_side(target):
    """
    Given a total weight for one side of the bar, return a list of tuples that
    total the desired weight.
    """
    if target == BARBELL:
        return [(0,)]
    solutions = []
    for n in range(len(WEIGHTS)+1):
        combos = combinations(WEIGHTS, n)
        for i in list(combos):
            if sum(i) == target and i not in solutions:
                solutions.append(i)
    return solutions

print(weights_for_side(45))
print(weights_for_side(70))
print(weights_for_side(15))


def weights_for_target(target):
    """
    Given a target mass to lift, return the available weight combinations to get to that mass.
    """
    side = weights_each_side(target)
    solutions = weights_for_side(side)
    if solutions:
        return solutions
    else:
        print(f"Can't make {side} lbs on each side with current weights!")

print(weights_for_target(105))
print(weights_for_target(50))
print(weights_for_target(45))
print(weights_for_target(15))


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
    spacing = diff / 4
    warmups = [
        BARBELL,
        BARBELL + spacing,
        BARBELL + 2*spacing,
        BARBELL + 3*spacing,
        workweight
    ]
    return warmups

print(find_warmups(105))
print(find_warmups(45))


def workout_calculator(workweight):
    """
    Given a workweight, return which plates to put on each side for each warmup set and the workset.
    """
    warmup_weights = find_warmups(workweight)
    for warmup in warmup_weights:
        print(warmup)
        print(weights_for_target(warmup))


print(workout_calculator(45))
print(workout_calculator(135))

# import pytest

# def test_weights_each_side():
#     assert weights_each_side(135) == 45
