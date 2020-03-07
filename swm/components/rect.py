from swm.components import Point, Window, Screen


class CenteredRect:
    """
        A Rect centered in the parent rect.
    """

    def __init__(self, width, height, parent, offset=Point(0, 0)):
        """
            Defined by a width and a height.
        """
        self._width = width
        self._height = height
        self._offset = offset

        if isinstance(parent, Screen):
            self.parent = parent
        else:
            raise TypeError("Parent viewport must be a Screen")

    def get_parent_center(self):
        """
            Get the center of the parent as a Point
        """
        center_x = self.parent.width // 2
        center_y = self.parent.height // 2
        return Point(center_x, center_y)

    def _get_absolute_rect(self):
        """
            Get the :class:`Rect` of this object
        """
        half_width = self._width // 2
        half_height = self._height // 2

        left = self.get_parent_center().x - half_width + self._offset.x
        width = self._width
        top = self.get_parent_center().y - half_height + self._offset.y
        height = self._height
        return Rect(left, top, width, height)

    @property
    def width(self):
        return self._get_absolute_rect().width

    @property
    def height(self):
        return self._get_absolute_rect().height

    @property
    def left(self):
        return self._get_absolute_rect().left

    @property
    def right(self):
        return self._get_absolute_rect().right

    @property
    def top(self):
        return self._get_absolute_rect().top

    @property
    def bottom(self):
        return self._get_absolute_rect().bottom

    @property
    def origin(self):
        return self._get_absolute_rect().origin


class ScreenspaceRect:
    def __init__(self, left, top, width, height, parent):
        self._ss_left = left
        self._ss_top = top
        self._ss_width = width
        self._ss_height = height

        if isinstance(parent, Screen):
            self.parent = parent
        else:
            raise TypeError("Parent viewport must be a Screen")

    def _get_absolute_rect(self):
        left = self._ss_left
        if left < 0:
            left += self.parent.width

        width = self._ss_width
        if width < 0:
            right = width + self.parent.width + 1
            width = right - left

        top = self._ss_top
        if top < 0:
            top += self.parent.height

        height = self._ss_height
        if height < 0:
            bottom = height + self.parent.height + 1
            height = bottom - top

        return Rect(left, top, width, height)

    @property
    def width(self):
        return self._get_absolute_rect().width

    @width.setter
    def width(self, new_width):
        self.__ss_right = self._ss_left + int(new_width)

    @property
    def height(self):
        return self._get_absolute_rect().height

    @height.setter
    def height(self, new_height):
        self.__ss_bottom = self._ss_top + int(new_height)

    @property
    def left(self):
        return self._get_absolute_rect().left

    @property
    def right(self):
        return self._get_absolute_rect().right

    @property
    def top(self):
        return self._get_absolute_rect().top

    @property
    def bottom(self):
        return self._get_absolute_rect().bottom

    @property
    def origin(self):
        return self._get_absolute_rect().origin

    def translate(self, vector_point):
        self._ss_left += vector_point.x
        self._ss_top += vector_point.y


class Rect:
    """
        A static rectangle
    """

    def __init__(self, origin_x, origin_y, width, height):
        self.origin = Point(origin_x, origin_y)
        self._width = width
        self._height = height

    def __str__(self):
        return str((self.origin.x, self.origin.y, self.width, self.height))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = int(new_width)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = int(new_height)

    @property
    def left(self):
        return self.origin.x

    @property
    def right(self):
        return self.origin.x + self.width

    @property
    def top(self):
        return self.origin.y

    @property
    def bottom(self):
        return self.origin.y + self.height

    def translate(self, vector_point):
        self.origin += vector_point
