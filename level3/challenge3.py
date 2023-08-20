"""
You're given a map represented as a matrix of 0s and 1s, where 0s are
passable space and 1s are impassable walls. The map entrance is at the top
left (0,0) and the exit is at the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest path
from the entrance to the exit, where you are allowed to remove one wall.  The
path length is the total number of nodes you pass through, counting both the
entrance and exit nodes.  The entrance and exit positions are always passable
(0). The map will always be solvable, though you may or may not need to
remove a wall. The height and width of the map can be from 2 to 20. Moves
can only be made in cardinal directions; no diagonal moves are allowed.
"""

testcase1 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]
# Expected output: 11

testcase2 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]
# Expected output: 7


def solution(map):
    """Work in progress"""
    pass
