#!/usr/bin/python3
import time
from swm import silica, Key, Screen, CheckList, TextBuffer

silica.setup()


class CheckItem:
    def __init__(self, name):
        self.checked = False
        self.name = name

    def toggle_checked(self):
        self.checked = not self.checked

    def __str__(self):
        return self.name


class Program:
    def __init__(self):
        silica.add_window((0, 0, 22, -1), "sidebar").set_theme("normal").set_title("Menu")
        silica.add_window((22, 0, -1, -1), "main_window").set_theme("double").set_title("Main program window")
        self.overlay = silica.add_centered_window((30, 5), "overlay").set_title("time.time()").set_theme("solid")

        # self.sidebar_menu = Menu(["First option", "Second option", "Third option", "Four"])
        check_list = [
            CheckItem(name) for name in ["First item", "Second item", "Third item", "Fourth item", "Fifth item"]
        ]
        self.sidebar_menu = CheckList(check_list)

        self.textbuffer = TextBuffer()

    def main(self):
        key_pressed = silica.get_keypress()
        if key_pressed == "Q":
            quit()
        elif key_pressed == Key.UP:
            self.sidebar_menu.previous()
        elif key_pressed == Key.DOWN:
            self.sidebar_menu.next()
        elif key_pressed == Key.BACKSPACE:
            self.textbuffer.backspace()
        elif key_pressed == Key.SPACE:
            self.sidebar_menu.toggle_selected_item_checked()

        self.textbuffer.add_keycode(key_pressed)

        main_window = silica.get_window("main_window")
        sidebar = silica.get_window("sidebar")
        overlay = silica.get_window("overlay")

        main_window.draw((1, 1), "Press up and down to interact with the menu on the left.", colour="white")
        main_window.draw((1, 2), "Type to enter text below:", colour="lightpurple")
        main_window.draw((1, 3), ">> " + self.textbuffer.get())

        screen = Screen(26, 5)
        screen.draw((0, 0), "Blue text", colour="blue")
        screen.draw((0, 1), "Flashing red text")
        screen.draw((0, 2), "Yellow underlined text", underline=True, colour="yellow")
        screen.draw((0, 3), "Reversed flashing red text", reverse=True)
        screen.draw((0, 4), "Cyan underlined bold text", bold=True, underline=True, colour="cyan")

        time_toggle = time.time() * 2 // 1 % 2 == 1
        if time_toggle:
            main_window.draw((2, -6), screen)
        else:
            main_window.draw((2, -6), screen, colour="red")
        overlay.draw((0, 1), str(time.time()).ljust(18).center(overlay.screen.width))

        sidebar_screen = self.sidebar_menu.render(sidebar.width, sidebar.height)
        sidebar.draw((1, 1), sidebar_screen)

        silica.process()


try:
    p = Program()
    while True:
        p.main()
except BaseException as e:
    silica.cleanup()
    raise e
