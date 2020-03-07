"""
Methods to override when extending:
    convert_item_to_string(item)
    convert_selected_item_to_string(item)
"""


from swm.components import Screen, Point
import unicodedata


class _BaseList:
    def __init__(self, contents):
        self.pointer = 0
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def _move_pointer(self, by_amount):
        self.pointer += by_amount
        self._limit_pointer()

    def _limit_pointer(self):
        top_index = len(self) - 1
        while not 0 <= self.pointer <= top_index:
            if self.pointer < 0:
                self.pointer += top_index + 1
            elif self.pointer > top_index:
                self.pointer -= top_index + 1

    def next(self):
        self._move_pointer(1)

    def previous(self):
        self._move_pointer(-1)

    @property
    def selected_item(self):
        self._limit_pointer()
        return self.contents[self.pointer]

    def _convert_item_to_string(self, item):
        return " " + str(item)

    def _convert_selected_item_to_string(self, item):
        return "[" + str(item) + "]"

    def render(self, width, height) -> Screen:
        render_screen = Screen(width, height)
        scroll_threshold = int(height / 2)

        sub_contents = self.contents
        if self.pointer < height - scroll_threshold:
            sub_contents = self.contents[:height]
        elif self.pointer > len(self.contents) - scroll_threshold:
            sub_contents = self.contents[-height:]
        else:
            sub_contents = self.contents[self.pointer - height + scroll_threshold : self.pointer + scroll_threshold]

        for index, item in enumerate(sub_contents):
            render_screen = self._render_item(Point(0, index), item, render_screen)
        if sub_contents[0] != self.contents[0]:
            render_screen.draw((-1, 0), unicodedata.lookup("UPWARDS ARROW"))
        if sub_contents[-1] != self.contents[-1]:
            render_screen.draw((-1, -1), unicodedata.lookup("DOWNWARDS ARROW"))
        return render_screen

    def _render_item(self, offset, item, render_screen):
        if item == self.selected_item:
            render_screen.draw(offset, self._convert_selected_item_to_string(item), bold=True, colour="yellow")
        else:
            render_screen.draw(offset, self._convert_item_to_string(item))
        return render_screen

    def render_to_window(self, window, offset=(0, 0)):
        rendered_menu = self.render(window.screen.width, window.screen.height)
        window.draw(offset, rendered_menu)

