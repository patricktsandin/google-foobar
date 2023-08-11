def solution(data, n):
    """
    Given a list of ID numbers and a limit, return the list without the ID
    numbers which appear more often than the limit.
    solution([1, 1, 2, 3, 3, 3, 4, 5], 2) --> [2, 4, 5]
    """
    counter = {}
    for id_number in data:
        if id_number not in counter:
            counter[id_number] = 1
        else:
            counter[id_number] += 1
    data = [
        id_number
        for id_number in data
        if counter[id_number] <= n
    ]
    return data
