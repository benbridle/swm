from swm.components import Point, ScreenCell, TextAttributes
import copy


class Screen:
    def __init__(self, width, height):
        self.size = Point(width, height)
        self.clear()

    def clear(self):
        self.contents = [[ScreenCell()] * self.size.x for _ in range(self.size.y)]

    def as_list(self):
        return self.contents

    @property
    def width(self):
        return self.size.x

    @width.setter
    def width(self, new_width):
        self.size.x = new_width
        self.clear()

    @property
    def height(self):
        return self.size.y

    @height.setter
    def height(self, new_height):
        self.size.y = new_height
        self.clear()

    def draw(self, offset, content, underline=False, reverse=False, bold=False, colour=None):
        attributes = TextAttributes(underline=underline, reverse=reverse, bold=bold, colour=colour)

        offset = Point(offset)
        if isinstance(content, (int, float)):
            content = str(content)

        if isinstance(content, Screen):
            self._draw_screen(offset, content, attributes=attributes)
            return

        if isinstance(content, list):
            for index, text in enumerate(content):
                line_offset = copy.copy(offset)  # needs to be copied, not referenced
                line_offset.y += index
                self._draw_string(line_offset, str(text), attributes=attributes)
            return

        if isinstance(content, str):
            self._draw_string(offset, content, attributes=attributes)
            return

        raise TypeError("Can't draw object of type {type}".format(type=type(content)))

    def _draw_screen(self, offset, screen, attributes=None):
        for index, line in enumerate(screen.as_list()):
            line_offset = Point(offset.x, offset.y + index)
            for cell in line:
                cell.attributes |= attributes
            self._draw_screencell_array(line_offset, line)

    def _draw_string(self, offset, content: str, attributes=None):
        content = [ScreenCell(char, attributes=attributes) for char in content]
        self._draw_screencell_array(offset, content)

    def _draw_screencell_array(self, offset, screencell_array):
        offset = Point(offset)
        try:
            screen_line = self.contents[offset.y]
        except IndexError:  # trying to draw off screen
            return
        for index, screencell in enumerate(screencell_array):
            try:
                screen_line[offset.x + index] = screencell
            except IndexError:
                pass
