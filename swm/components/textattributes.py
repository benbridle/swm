import curses

class TextAttributes:
    DIM = curses.A_DIM
    BOLD = curses.A_BOLD
    REVERSE = curses.A_REVERSE
    UNDERLINE = curses.A_UNDERLINE

    COLOURS = {
        "foreground": 0,
        "background": 1,
        "red": 2,
        "green": 3,
        "yellow": 4,
        "blue": 5,
        "purple": 6,
        "cyan": 7,
        "lightgrey": 8,
        "grey": 9,
        "lightred": 10,
        "lightgreen": 11,
        "lightyellow": 12,
        "lightblue": 13,
        "lightpurple": 14,
        "lightcyan": 15,
        "white": 16,
        "black": 17,
        }

    def __init__(self, colour=None, underline=False, bold=False, dim=False, reverse=False):
        self.underline = underline
        self.dim = dim
        self.bold = bold
        self.reverse = reverse
        self.colour = colour

    def __int__(self):
        return self.to_curses()

    def __repr__(self):
        shorthand = ""
        for letter, attr in zip("CUBDR", (self.colour, self.underline, self.bold, self.dim, self.reverse)):
            if attr:
                shorthand += letter
        return "TextAttributes(" + shorthand + ")"

    def __or__(self, other):
        self.underline |= other.underline
        self.bold |= other.bold
        self.reverse |= other.reverse
        self.dim |= other.dim
        if self.colour is None:
            self.colour = other.colour
        return self

    def to_curses(self):
        attr = 0
        if self.underline: attr |= TextAttributes.UNDERLINE
        if self.dim: attr |= TextAttributes.DIM
        if self.reverse: attr |= TextAttributes.REVERSE
        if self.bold: attr |= TextAttributes.BOLD
        if self.colour is not None:
            try:
                attr |= curses.color_pair(TextAttributes.COLOURS[self.colour.lower()])
            except:
                raise KeyError("No colour with name '" + str(self.colour) + "'")
        return attr
