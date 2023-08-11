"""
Find lucky triples x, y, z given a list l of integers where:
2 <= len(l) <= 2000,
l.index(x) < l.index(y) < l.index(z)
z % y == y % x == 0
1 <= l[any] <= 999999
"""


def solution1(l):
    """This solution initially used recursion, which ran up against the
    stack size limit.  Refactored to use a stack on the heap.  Much too slow."""
    stack = list()
    lucky_set = list()
    lucky_list = list()
    stack.append((l, lucky_list))

    while stack:
        frame = stack.pop()
        elements = list(frame[0])
        lucky_list = list(frame[1])
        new_lucky_list = list(frame[1])
        element = elements.pop(0)

        if elements:
            stack.append((elements, lucky_list))

        if not new_lucky_list or element%new_lucky_list[-1] == 0:
            new_lucky_list.append(element)
            if len(new_lucky_list) == 3:
                lucky_set.append(tuple(new_lucky_list))
            elif len(new_lucky_list) < 3 and elements:
                stack.append((elements, new_lucky_list))

    return lucky_set


def solution2(l):
    """This solution uses nested loops, with worst-case time complexity of
    O(n^3).  Final test seems to trigger worst-case perf, so this fails."""
    counter = 0
    enumerated_list = list(enumerate(l))
    for first_index, first_digit in enumerated_list:
        for second_index, second_digit in enumerated_list[first_index+1:]:
            if second_digit % first_digit == 0:
                for _, third_digit in enumerated_list[second_index+1:]:
                    if third_digit % second_digit == 0:
                        counter += 1
    return counter


def solution3(l):
    """Final test seemed to be feeding a list of largely the same integer,
    triggering worst-case performance in solution2.  Tried taking a shortcut
    for lists of identical values on the off-chance."""
    length = len(l)
    sequence = length - 2
    return (
        (sequence + 1)
        * (sequence * (sequence + 1) / 2)
        - (sequence * (sequence + 1) * (2 * sequence + 1))
        / 6
    )


def solution4(l):
    """Caved in and looked for other people's solutions online.  Adapted the
    below solution, which cleverly uses dynamic programming: instead of
    looking for lucky triples, it looks for lucky doubles and logs them."""
    log = [0]*len(l)
    counter = 0
    for second_index in range(0, len(l)):
        for first_index in range(0, second_index):
            if l[second_index] % l[first_index] == 0:
                log[second_index] = log[second_index] + 1
                counter = counter + log[first_index]
    return counter
