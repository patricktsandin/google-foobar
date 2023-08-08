def solution(data, n):
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
