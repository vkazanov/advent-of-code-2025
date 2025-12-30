from enum import Enum

class COLOR(Enum):
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34

class FORMAT(Enum):
    BOLD = 1
    UNDERLINE = 4

# see https://en.wikipedia.org/wiki/ANSI_escape_code
class CONTROL(Enum):
    ERASE_IN_LINE = "\033[K"
    CURSOR_UP = "\033[A"
    CURSOR_DOWN = "\033[B"
    CURSOR_FORWARD = "\033[C"
    CURSOR_BACK = "\033[D"
    CR = "\r"
    NL = "\n"

def cstr(obj, color=COLOR.BLUE, fmt=FORMAT.BOLD):
    return f"\033[{fmt.value};{color.value}m{obj}\033[0m"

class Vec:
    """Immutable vectorx"""

    __slots__ = ("_data",)

    def __init__(self, values):
        data = tuple(values)
        if not data:
            raise ValueError("Vector cannot be empty")
        self._data = data

    @classmethod
    def of(cls, *values):
        return cls(values)

    def __repr__(self):
        return "Vec(" + ", ".join(map(str, self._data)) + ")"

    def __hash__(self):
        return hash(self._data)

    def __eq__(self, other):
        return isinstance(other, Vec) and self._data == other._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def _check_dim(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension mismatch")

    def _check_2d(self):
        if len(self._data) != 2:
            raise ValueError("Direction methods require a 2D vector")

    @property
    def x(self):
        if len(self._data) < 1:
            raise AttributeError("x is not defined")
        return self._data[0]

    @property
    def y(self):
        if len(self._data) < 2:
            raise AttributeError("y is not defined")
        return self._data[1]

    # arithmetic
    def __add__(self, other):
        if not isinstance(other, Vec):
            return NotImplemented
        self._check_dim(other)
        return Vec(a + b for a, b in zip(self._data, other._data))

    def __sub__(self, other):
        if not isinstance(other, Vec):
            return NotImplemented
        self._check_dim(other)
        return Vec(a - b for a, b in zip(self._data, other._data))

    def __neg__(self):
        return Vec(-a for a in self._data)

    def __mul__(self, k):
        return Vec(a * k for a in self._data)

    def __rmul__(self, k):
        return self.__mul__(k)

    # directional helpers (2D, screen coordinates)
    def up(self):
        self._check_2d()
        x, y = self._data
        return Vec((x, y - 1))

    def down(self):
        self._check_2d()
        x, y = self._data
        return Vec((x, y + 1))

    def left(self):
        self._check_2d()
        x, y = self._data
        return Vec((x - 1, y))

    def right(self):
        self._check_2d()
        x, y = self._data
        return Vec((x + 1, y))
