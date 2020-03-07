class TextBuffer:
    def __init__(self):
        self.clear()

    def __str__(self):
        return self.buffer

    def get(self):
        return self.buffer

    def clear(self):
        self.buffer = ""

    def add(self, text):
        self.buffer += str(text)

    def add_keycode(self, keycode):
        keycode = int(keycode)
        if keycode > 128 or keycode == -1:
            return
        character = chr(keycode)
        self.buffer += character

    def backspace(self):
        self.buffer = self.buffer[:-1]
