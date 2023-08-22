"""
You're given a maze represented as a matrix of 0s and 1s, where 0s are
passable space and 1s are impassable walls. The maze entrance is at the top
left (0,0) and the exit is at the bottom right (w-1,h-1).

Write a function solution(maze) that generates the length of the shortest path
from the entrance to the exit, where you are allowed to remove one wall.  The
path length is the total number of nodes you pass through, counting both the
entrance and exit nodes.  The entrance and exit tiles are always passable
(0). The maze will always be solvable, though you may or may not need to
remove a wall. The height and width of the maze can be from 2 to 20. Moves
can only be made in cardinal directions; no diagonal moves are allowed.
"""


maze1 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]
# Expected output: 11


maze2 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]
# Expected output: 7


maze3 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
]

maze4 = [
    [0, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [0, 0],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 0],
]

maze5 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
]

maze6 = [
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


maze7 = [
    [0, 1],
    [1, 0]
]


class Maze:
    """Given a maze, find the shortest path after removing up to one wall."""
    def __init__(self, maze, distances=None):
        self.maze = maze
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.height = len(maze)
        self.width = len(maze[0])
        self.entrance = (0, 0)
        self.exit = (self.height - 1, self.width - 1)
        self.neighbors = dict()
        self.distances = distances or dict()
        self.pathway = self.get_contiguous(self.entrance)
        self.shortest_possible_path = self.height + self.width - 1
        self.is_solveable = self.exit in self.pathway
        self.walls = self.get_walls()
        if self.is_solveable:
            self.initialize_neighbors()
            self.initialize_distances()
            self.generate_shortest_paths()
            self.shortest_path = self.distances[self.exit]

    def generate_shortest_paths(self):
        for destination in self.neighbors[self.entrance]:
            self.distances[destination] = 2

        changed = True
        while changed:
            changed = False
            for source, destinations in self.neighbors.items():
                for destination in destinations:
                    if self.distances[destination] > self.distances[source] + 1:
                        self.distances[destination] = self.distances[source] + 1
                        changed = True

    def get_maze_without_wall(self, maze, wall):
        while wall:
            tile = wall.pop()
            self.set_tile(maze, tile, 0)
        return maze

    def initialize_neighbors(self):
        for tile in self.pathway:
            self.neighbors[tile] = self.get_destinations(tile)

    def initialize_distances(self):
        for tile in self.pathway:
            if tile not in self.distances:
                self.distances[tile] = float("inf")
        self.distances[self.entrance] = 1

    def get_walls(self):
        tiles = set(self.get_tiles())
        walls = []
        while tiles:
            tile = tiles.pop()
            contiguous = self.get_contiguous(tile)
            tiles.difference_update(contiguous)
            if self.get_tile(self.maze, tile) == 1:
                walls.append(contiguous)
        return walls

    def get_contiguous(self, source):
        checked = {source}
        to_be_checked = {source}
        contiguous = {source}
        while to_be_checked:
            checking = to_be_checked.pop()
            destinations = self.get_destinations(checking)
            for destination in destinations:
                contiguous.add(destination)
                if destination not in checked:
                    to_be_checked.add(destination)
            checked.add(checking)
        return contiguous

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
                self.get_tile(self.maze, source)
                == self.get_tile(self.maze, destination)
            )
        )

    def get_tiles(self):
        return [
            (row, column)
            for row in range(self.height)
            for column in range(self.width)
        ]

    @staticmethod
    def set_tile(maze, tile, value):
        maze[tile[0]][tile[1]] = value

    @staticmethod
    def get_tile(maze, tile):
        return maze[tile[0]][tile[1]]


def solution(map):
    mazes = []
    initial_maze = Maze(map)
    if initial_maze.is_solveable:
        mazes.append(initial_maze)
    for wall in initial_maze.walls:
        submaze = Maze(
            maze=initial_maze.get_maze_without_wall(initial_maze.maze, wall),
            distances=initial_maze.distances
        )
        if submaze.is_solveable:
            mazes.append(submaze)

    shortest_path = float("inf")
    for maze in mazes:
        if maze.shortest_path < shortest_path:
            shortest_path = maze.shortest_path
    print shortest_path


solution(maze1)
solution(maze2)
solution(maze3)
solution(maze4)
solution(maze5)
solution(maze6)
solution(maze7)
