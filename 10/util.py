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
