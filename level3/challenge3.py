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


class Maze:
    """Work in progress"""
    def __init__(self, map):
        self.map = map
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.height = len(map)
        self.width = len(map[0])

    def solve(self):
        pass

    def get_walls(self):
        positions = set(self.get_positions())
        walls = []
        while positions:
            position = positions.pop()
            contiguous = self.get_contiguous(position)
            positions.difference_update(contiguous)
            if self.map[position[0]][position[1]] == 1:
                walls.append(contiguous)
        return walls

    def get_contiguous(self, source):
        checked = [source]
        to_be_checked = [source]
        contiguous = {source}
        while to_be_checked:
            checking = to_be_checked.pop(0)
            destinations = self.get_destinations(checking)
            for destination in destinations:
                contiguous.add(destination)
                if destination not in checked:
                    to_be_checked.append(destination)
            checked.append(checking)
        return list(contiguous)

    def get_destinations(self, source):
        destinations = []
        moves = self.get_valid_moves(source)
        for move in moves:
            destination = (source[0] + move[0], source[1] + move[1])
            destinations.append(destination)
        return destinations

    def get_valid_moves(self, source):
        return [
            move for move in self.moves
            if self.validate_move(source, move)
        ]

    def validate_move(self, source, move):
        destination = (source[0] + move[0], source[1] + move[1])
        return (
            0 <= destination[0] < self.height
            and 0 <= destination[1] < self.width
            and (
                self.map[source[0]][source[1]]
                == self.map[destination[0]][destination[1]]
            )
        )

    def get_positions(self):
        return [
            (row, column)
            for row in range(self.height)
            for column in range(self.width)
        ]


maze = Maze(testcase2)

print(
    maze.get_walls()
)
