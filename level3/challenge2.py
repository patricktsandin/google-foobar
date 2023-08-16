"""
Input is a description of a probabilistic automaton/Markov chain represented
as a matrix m, an array of arrays of integers.  The index in diagonal positions
m[0][0] to m[-1][-1] represents the current state.  All other indexes represent
alternative states.  The integer at each position within a given array --
divided by the sum of the array -- represents the dest_state of probabilitying
into that position.  Arrays for which all non-current indexes are 0 indicate
the current index is terminal, with no further probabilitys possible.

The task is to calculate the probabilities of terminating in each terminal
position.
"""


from fractions import Fraction, gcd


def get_stable_states(states):
    return [sum(state) == 0 for state in states]


def numerators_to_fractions(integers):
    denominator = (sum(integers) or 1)
    return [Fraction(numerator, denominator) for numerator in integers]


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def simplest_form(fractions):
    fractions = [
        fraction.limit_denominator(max_denominator=10000) for fraction in fractions
    ]
    least_common_multiple = reduce(
        lcm, [fraction.denominator for fraction in fractions]
    )
    return [
         int(fraction.numerator * least_common_multiple // fraction.denominator)
         for fraction in fractions
    ] + [int(least_common_multiple)]


def collapse_probabilities(probabilities):
    return [sum(probability_set) for probability_set in probabilities]


def dest_probabilities(probabilities, stable_states):
    return [
        prob for index, prob in enumerate(probabilities)
        if stable_states[index]
    ]


def solution(states):
    states = [numerators_to_fractions(state) for state in states]
    state_count = len(states)
    queue = [(1, 0)]
    stable_states = get_stable_states(states)
    probabilities = [[Fraction(0, 1)] for _ in states]

    while queue:
        previous_probability, state = queue.pop(0)
        for dest_state in range(state_count):
            dest_probability = states[state][dest_state]
            if dest_probability > 0:
                probabilities[dest_state].append(
                    dest_probability * previous_probability
                )
                if (
                    not stable_states[dest_state]
                    and probabilities[dest_state][-1] > Fraction(1, 1000000000)
                ):
                    queue.append((probabilities[dest_state][-1], dest_state))

    probabilities = collapse_probabilities(probabilities)
    probabilities = dest_probabilities(probabilities, stable_states)
    return simplest_form(probabilities)
