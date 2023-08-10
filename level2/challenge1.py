"""
Given a chessboard with tiles numbered 0-63 left-to-right and top-to-bottom,
return the minimum number of moves for a knight to move from a given source
to a given destination tile.
"""


moves = (
    (-8, -2), (-16, -1), (-16, 1), (-8, 2), (8, -2), (16, -1), (16, 1), (8, 2)
)

board = list(range(64))


def validate_move(source, vertical, horizontal):
    return (
        0 <= (source + vertical) < len(board)
        and 0 <= ((source % 8) + horizontal) <= 7
    )


def generate_destinations(source):
    destinations = []
    for move in moves:
        if validate_move(source, move[0], move[1]):
            destinations.append(source + move[0] + move[1])
    return destinations


def initialize_distances(source):
    distances = {}
    for tile in board:
        distances[tile] = float("inf")
    distances[source] = 0
    return distances


def initialize_neighbor_list():
    neighbors = {}
    for tile in board:
        neighbors[tile] = generate_destinations(tile)
    return neighbors


def solution(src, dest):
    distances = initialize_distances(src)
    neighbors = initialize_neighbor_list()

    for destination in neighbors[src]:
        distances[destination] = 1

    changed = True
    while changed:
        changed = False
        for source, destinations in neighbors.items():
            for destination in destinations:
                if distances[destination] > distances[source] + 1:
                    distances[destination] = distances[source] + 1
                    changed = True

    return distances[dest]
