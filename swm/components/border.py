class Border:
    NORMAL = "┌┐└┘─│┼"
    SOLID = "┏┓┗┛━┃╋"
    DOUBLE = "╔╗╚╝═║╬"
    ASCII = "++++-|+"
    NONE = "       "
    MINIMAL = "┌┐└┘ │ "

    TOPLEFT = 0
    TOPRIGHT = 1
    BOTTOMLEFT = 2
    BOTTOMRIGHT = 3
    HORIZONTAL = 4
    VERTICAL = 5
    INTERSECTION = 6

    @classmethod
    def get_theme(cls, theme_name):
        theme_name = theme_name.upper()
        if theme_name == "NORMAL":
            return cls.NORMAL
        elif theme_name == "SOLID":
            return cls.SOLID
        elif theme_name == "DOUBLE":
            return cls.DOUBLE
        elif theme_name == "ASCII":
            return cls.ASCII
        elif theme_name == "NONE":
            return cls.NONE
        elif theme_name == "MINIMAL":
            return cls.MINIMAL
        else:
            raise ValueError("No theme named {theme_name}")