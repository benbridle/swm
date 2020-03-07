import curses
from swm.components import TextAttributes


class ScreenCell:
    # , colour="white", background_colour
    def __init__(self, character=" ", attributes=None):
        self.set_character(character)
        if attributes is None:
            self.attributes = TextAttributes()
        else:
            self.attributes = attributes

    def set_character(self, new_character):
        if not (len(new_character) == 1 and isinstance(new_character, str)):
            raise TypeError("Character must be a single character string")
        self.character = new_character

    def __repr__(self):
        return "ScreenCell('" + self.character + "')"
