"""
.. module:: Key
   :synopsis: Key class for cwm
.. moduleauthor:: Ben Bridle <github.com/benbridle>
"""

import string
key_name_to_key_code = {

    "UP": 259,
    "DOWN": 258,
    "LEFT": 260,
    "RIGHT": 261,

    "SPACE": 32,
    "ENTER": 10,
    "BACKSPACE": 263,
    "DELETE": 330,
    "DOT": 46,
    "ESCAPE": 27,
    "PAGEUP": 339,
    "PAGEDOWN": 338,
}


class Key:
    UP = 259
    DOWN = 258
    LEFT = 260
    RIGHT = 261

    SPACE = 32
    ENTER = 10
    BACKSPACE = 263
    DELETE = 330
    DOT = 46
    ESCAPE = 27
    PAGEUP = 339
    PAGEDOWN = 338

    @staticmethod
    def letter(letter):  # case sensitive
        """
            Get key code for letter.
        """
        if not (isinstance(letter, str) and len(letter) == 1):
            raise ValueError("Input must be a one character string")
        return ord(letter)

    @classmethod
    def character_range(cls, characters):
        return [cls.letter(char) for char in characters]


class KeyCode:
    def __init__(self, key_code: int):
        self.code = key_code

    def __str__(self):
        if chr(self.code) in string.ascii_letters + string.digits + string.punctuation:
            return chr(self.code)
        else:
            return ""

    def to_char(self):
        pass


class KeyPress:
    def __init__(self, keycode: int):
        self.code = keycode

    def __str__(self):
        """If keycode represents a character key, return that character"""
        if self.is_empty():
            return ""
        if chr(self.code) in string.ascii_letters + string.digits + string.punctuation:
            return chr(self.code)
        else:
            return ""

    def __int__(self):
        return self.code

    def __eq__(self, other):
        if isinstance(other, str):
            return self.__str__() == other
        if isinstance(other, int):
            return self.__int__() == other
        raise TypeError(f"Can't compare equality to type {type(other)}")

    def is_empty(self):
        if self.code == -1:
            return True
        return False

    def is_character(self):
        if self.__str__() != "":
            return True
        return False