"""
Input is a description of a probabilistic automaton/Markov chain represented
as a matrix m, an array of arrays of integers.  The index in diagonal positions
m[0][0] to m[-1][-1] represents the current state.  All other indexes represent
alternative states.  The integer at each position within a given array --
divided by the sum of the array -- represents the probability of transitioning
into that position.  Arrays for which all non-current indexes are 0 indicate
the current index is terminal, with no further transitions possible.

The task is to calculate the probabilities of terminating in each terminal
position.
"""


import operator
from decimal import Decimal
from fractions import Fraction, gcd
from itertools import chain

m = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


n = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def get_stable_states(samples):
    return [sum(sample) == 0 for sample in samples]


def numerators_to_decimals(integers):
    denominator = Decimal(sum(integers) or 1)
    return [Decimal(integer) / denominator for integer in integers]


def denominators_from_fractions(fractions):
    return [fraction.denominator for fraction in fractions]


def greatest_common_multiplier(fractions):
    return reduce(gcd, chain.from_iterable(fractions))


def multiply(numbers):
    return reduce(operator.mul, numbers)


def equalize_fractions(fractions):
    denominators = denominators_from_fractions(fractions)
    super_denominator = multiply(denominators)
    for index, fraction in enumerate(fractions):
        multiplier = super_denominator / fraction.denominator
        fractions[index] = (
            fraction.numerator * multiplier,
            fraction.denominator * multiplier
        )
    gcm = greatest_common_multiplier(fractions)
    for index, fraction in enumerate(fractions):
        fractions[index] = (fraction[0] / gcm, fraction[1] / gcm)
    return fractions


def solution(samples):
    samples = [numerators_to_decimals(sample) for sample in samples]
    iterations = 10000
    queue = [(1, 0)]
    stable_states = get_stable_states(samples)
    probabilities = [[] for _ in samples]

    while iterations > 0 and queue:
        iterations -= 1
        previous_probability, sample_id = queue.pop(0)
        for transition in range(len(samples[sample_id])):
            if samples[sample_id][transition]:
                probabilities[transition].append(
                    samples[sample_id][transition] * previous_probability
                )
            if not stable_states[transition] and samples[sample_id][transition] != 0:
                queue.append((probabilities[transition][-1], transition))

    fractions = []
    for index, probability_set in enumerate(probabilities):
        if stable_states[index]:
            fractions.append(Fraction(sum(probability_set)).limit_denominator())

    fractions = equalize_fractions(fractions)
    denominator = fractions[0][1]
    result = []
    for fraction in fractions:
        result.append(int(fraction[0]))
    result.append(int(denominator))
    return result

#
print(solution(m))
print(solution(n))

# print(get_stable_states(n))

# print(convert_to_decimal(m))