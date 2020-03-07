import time
import os
import curses
import operator

from swm.components import Screen, Window, ScreenspaceRect, CenteredRect, KeyPress


class SilicaWindowManager:
    """
    Main object that handles window manager state.
    """

    DEFAULT_DELAY = 0.01  # Delay in seconds between full redraws

    def __init__(self):
        self._windows = {}
        self.viewport = Screen(0, 0)
        self._recalculate_screen_size()
        self.set_delay(self.DEFAULT_DELAY)

    def setup(self):
        """
        Explicitly prepare the terminal for drawing to. This will mess up
        the terminal for normal operations, and will need to be reversed on
        exit by calling cleanup()
        """
        self._curses_setup()

    def set_delay(self, new_delay):
        self.delay = new_delay  # seconds

    def _curses_setup(self):
        self.scr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.scr.keypad(True)
        self.scr.scrollok(False)
        self.scr.nodelay(True)

    @staticmethod
    def cleanup():
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        curses.curs_set(1)

    def _recalculate_screen_size(self):
        """
        Updates viewport size to be the current terminal size and recalculates all windows.
        """
        x, y = os.get_terminal_size()
        self.viewport.width = x
        self.viewport.height = y
        for window in self._windows.values():
            window._generate_screen()

    def add_window(self, screenspace_rect, identifier) -> Window:
        return self._add_window(ScreenspaceRect(*screenspace_rect, self.viewport), identifier)

    def add_centered_window(self, centered_rect, identifier):
        return self._add_window(CenteredRect(*centered_rect, self.viewport), identifier)

    def _add_window(self, rect, identifier):
        if identifier in self._windows.keys():
            raise ValueError("A window with this identifier already exists")

        new_window = Window(rect)
        new_window.identifier = identifier

        z_index = 0
        for window in self._windows.values():
            z_index = max(window.z_index, z_index + 1)
        new_window.z_index = z_index

        self._windows[identifier] = new_window
        return new_window

    def get_window(self, identifier):
        try:
            return self._windows[identifier]
        except KeyError:
            raise KeyError("No window with this identifier exists")

    def get_keypress(self):
        return KeyPress(self.scr.getch())

    def process(self):
        self.draw_windows()
        self.render()
        self.scr.refresh()
        self._recalculate_screen_size()
        time.sleep(self.delay)

    def draw_windows(self):
        for window in sorted(self._windows.values(), key=operator.attrgetter("z_index")):
            if not window.visible:
                continue
            rendered_window = window.render()
            self.viewport.draw(window.rect.origin, rendered_window)
            window.screen.clear()

    def safe_error(self, e):
        self.cleanup()
        raise e

    def render(self):
        for y_index, line in enumerate(self.viewport.as_list()):
            try:
                if y_index == self.viewport.size.height - 1:
                    self.scr.insnstr(y_index, self.viewport.size.width - 1, line[-1].character, 0)
                    line = line[:-1]
                for x_index, screencell in enumerate(line):
                    self.scr.addstr(y_index, x_index, screencell.character, screencell.attributes.to_curses())
            except curses.error as e:
                pass
                # self.safe_error(e)
