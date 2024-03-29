"""Locations for the simulation"""

from __future__ import annotations


class Location:
    """A two-dimensional location.

    === Attributes ===
    row:
        A value representing the horizontal index
    col:
        A value representing the vertical index
    """
    row: int
    col: int

    def __init__(self, row: int, column: int) -> None:
        """Initialize a location.

        """
        self.row = row
        self.col = column

    def __str__(self) -> str:
        """Return a string representation.
        """
        x = str(self.row)
        y = str(self.col)
        s = "("
        s += x
        s += ", " + y
        s += ")"
        return s

    def __eq__(self, other: Location) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self.row == other.row and self.col == other.col


def manhattan_distance(origin: Location, destination: Location) -> int:
    """Return the Manhattan distance between the origin and the destination.

    """
    return abs(origin.col - destination.col) + abs(origin.row - destination.row)


def deserialize_location(location_str: str) -> Location:
    """Deserialize a location.

    location_str: A location in the format 'row,col'
    """
    loc = location_str.split(',')
    return Location(int(loc[0]), int(loc[1]))


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
