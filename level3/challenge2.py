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

from decimal import Decimal
from fractions import Fraction

m = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


def get_stable_states(samples):
    stable_states = []
    for sample in samples:
        is_stable = sum(sample) == 0
        stable_states.append(is_stable)
    return stable_states


def convert_to_decimal(samples):
    for sample in samples:
        denominator = sum(sample)
        for transition, probability in enumerate(sample):
            if denominator == 0:
                probability = Decimal(0)
            else:
                probability = Decimal(
                    Decimal(probability) / Decimal(denominator)
                )
            sample[transition] = probability
    return samples


def solution(samples):
    samples = convert_to_decimal(samples)
    iterations = 10
    queue = [(1, 0)]
    stable_states = get_stable_states(samples)
    probabilities = [[]]*len(samples)

    # import pdb; pdb.set_trace()
    while iterations > 0:
        print ''
        print ''
        iterations -= 1
        print "Iterations:", iterations
        print "Queue", queue
        previous_probability, state = queue.pop(0)
        print "Prev prob:", previous_probability, "Prev state:", state
        sample_id = state
        print "Sample:", samples[sample_id]
        for transition in range(len(samples[sample_id])):
            print "This prob from record:", probabilities[transition]
            print "This prob from sample:", samples[sample_id][transition]
            import pdb; pdb.set_trace()
            if samples[sample_id][transition]:
                if probabilities[transition]:
                    probabilities[transition].append(
                        probabilities[transition][-1] * previous_probability
                    )
                else:
                    probabilities[transition].append(
                        samples[sample_id][transition] * previous_probability
                    )
            if not stable_states[transition] and samples[sample_id][transition] != 0:
                queue.append((probabilities[transition][-1], transition))
            print "Prob record:", probabilities

    print probabilities


solution(m)