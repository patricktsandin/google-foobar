def solution(x, y):
    """Given a 2D coordinate plane tiled with integers starting at coordinates
    (1,1) and layering diagonally, like so:
    7
    4 8
    2 5 9
    1 3 6 10
    return the integer at a given set of coordinates.
    """
    side_length = x + y - 1
    corner_value = (side_length * (side_length + 1)) / 2
    return corner_value - (y - 1)
