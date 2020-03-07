from swm.widgets import _BaseList


class Menu(_BaseList):
    def convert_item_to_string(self, item):
        return " " + str(item)

    def convert_selected_item_to_string(self, item):
        return "[" + str(item) + "]"
