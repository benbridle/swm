from swm.components import Screen, Point, Border


class Window:
    def __init__(self, rect, z_index=0):
        self.visible = True
        self.title = ""
        self.rect = rect
        self._generate_screen()
        self.theme = Border.NORMAL
        self.identifier = None
        self.z_index = z_index

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def _generate_screen(self):
        self.screen = Screen(self.rect.width - 2, self.rect.height - 2)

    def draw(self, *args, **kwargs):
        self.screen.draw(*args, **kwargs)

    def render(self) -> Screen:
        render_screen = Screen(self.rect.width, self.rect.height)

        top_edge = (
            self.theme[Border.TOPLEFT] + self.theme[Border.HORIZONTAL] * self.screen.width + self.theme[Border.TOPRIGHT]
        )

        if self.title != "":
            top_edge = (
                self.theme[Border.TOPLEFT]
                + " {title} ".format(title=self.title).center(self.screen.width, self.theme[Border.HORIZONTAL])
                + self.theme[Border.TOPRIGHT]
            )

        bottom_edge = (
            self.theme[Border.BOTTOMLEFT]
            + self.theme[Border.HORIZONTAL] * self.screen.width
            + self.theme[Border.BOTTOMRIGHT]
        )

        render_screen.draw((0, 0), top_edge)
        for y in range(self.screen.height):
            render_screen.draw((0, y + 1), self.theme[Border.VERTICAL])
            render_screen.draw(Point(self.screen.width + 1, y + 1), self.theme[Border.VERTICAL])
        render_screen.draw((0, self.rect.height - 1), bottom_edge)
        render_screen.draw(Point(1, 1), self.screen)

        return render_screen

    def auto_title(self):
        try:
            self.title = str(self.identifier)
            return self
        except ValueError:
            raise TypeError("Window identifier must be a valid string")

    def set_title(self, new_title):
        self.title = new_title
        return self

    def set_theme(self, theme_name):
        self.theme = Border.get_theme(theme_name)
        return self
