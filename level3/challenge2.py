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

def solution(m):
    pass  # TODO: research probabilistic automata and Markov chains tomorrow.
