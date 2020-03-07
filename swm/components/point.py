class Point:
    def __init__(self, one, two=None):
        self.x = 0
        self.y = 0
        self.set(one, two)

    def __tuple__(self):
        return self.as_tuple()

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        else:
            raise TypeError("Can only add a Point to a Point")

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Point(self.x * -1, self.y * -1)

    def __sub__(self, other):
        if isinstance(other, Point):
            return self.__add__(other.__neg__())
        else:
            raise TypeError("Can only subtract a Point from a Point")

    def __rsub__(self, other):
        raise NotImplementedError
        # TODO: Fix implementation here, I must've gotten confused with the order of neg and sub
        # if isinstance(other, Point):
        #     return self.__neg__(self.__sub__(other))
        # else:
        #     raise TypeError("Can only subtract a Point from a Point")

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return str(self.as_tuple())

    def as_tuple(self):
        return (self.x, self.y)

    def set(self, one, two=None):
        if two is None:
            if isinstance(one, Point):
                self.x = one.x
                self.y = one.y
            else:
                self.x = one[0]
                self.y = one[1]
        else:
            self.x = one
            self.y = two
        try:
            assert isinstance(self.x, int)
            assert isinstance(self.y, int)
        except AssertionError:
            raise TypeError("Points can only be constructed from two ints or a sequence of two ints")

    @property
    def width(self):
        return self.x

    @width.setter
    def width(self, new_value):
        self.x = new_value

    @property
    def height(self):
        return self.y

    @height.setter
    def height(self, new_value):
        self.y = new_value

