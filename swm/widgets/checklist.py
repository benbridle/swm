from swm.widgets import _BaseList


class CheckList(_BaseList):
    def convert_item_to_string(self, item):
        return self.get_checkbox_for_item(item) + "  " + str(item)

    def convert_selected_item_to_string(self, item):
        return self.get_checkbox_for_item(item) + "  " + str(item)

    def get_checkbox_for_item(self, item):
        if item.checked:
            checkbox = "[\u2713]"  # unicode tick character
        else:
            checkbox = "[ ]"
        return checkbox

    def toggle_selected_item_checked(self):
        self.selected_item.toggle_checked()
