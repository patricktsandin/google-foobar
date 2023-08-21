"""
You're given a map represented as a matrix of 0s and 1s, where 0s are
passable space and 1s are impassable walls. The map entrance is at the top
left (0,0) and the exit is at the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest path
from the entrance to the exit, where you are allowed to remove one wall.  The
path length is the total number of nodes you pass through, counting both the
entrance and exit nodes.  The entrance and exit tiles are always passable
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
        self.entrance = (0, 0)
        self.exit = (self.height - 1, self.width - 1)
        self.neighbors = dict()
        self.distances = dict()

    # def solve(self, wall_to_remove=None):
    #     pass
    #
    # def solve_submaps(self):
    #     pass

    def remove_wall(self, wall):
        while wall:
            tile = wall.pop()
            self.set_tile(tile, 0)

    def set_tile(self, tile, value):
        self.map[tile[0]][tile[1]] = value

    # def get_tile(self, tile):
    #     return self.map[tile[0]][tile[1]]

    def is_solveable(self):
        pathways = self.get_contiguous(self.entrance)
        return self.exit in pathways

    def get_walls(self):
        tiles = set(self.get_tiles())
        walls = []
        while tiles:
            tile = tiles.pop()
            contiguous = self.get_contiguous(tile)
            tiles.difference_update(contiguous)
            if self.map[tile[0]][tile[1]] == 1:
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

    def get_tiles(self):
        return [
            (row, column)
            for row in range(self.height)
            for column in range(self.width)
        ]

    # def get_passable_tiles(self):
    #     return [
    #         (row, column)
    #         for row in range(self.height)
    #         for column in range(self.width)
    #         if self.map[row][column] == 0
    #     ]


maze = Maze(testcase2)

print(
    maze.is_solveable()
)
