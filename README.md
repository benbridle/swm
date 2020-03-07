#Silica Window Manager

Silica is a simple terminal user interface framework for Python. It provides a simple API for getting user input, styling text, and drawing text inside windows. 


##Setup

Clone the project and run `pip3 install --no-index swm`. 

##Usage
At the top of your script add `from swm import silica`.

To add a window that fills the screen, call `silica.add_window((0,0,-1,-1), "big_window")`. `big_window` is a unique identifier that can be used to get a reference to the window.

Call `w = silica.get_window("big_window")` to get a window reference. 

To draw to the window, call `w.draw((0,0), "Hello world")`.

Finally, call `silica.process()` to update the screen with the changes we've made.

Text can be styled by using keyword arguments in the `draw()` function call. Try `bold=True`, `reverse=True`, `colour="yellow"`, and `underline=True`.

Get keypresses by calling `keypress = silica.get_keypress()`. This returns a KeyPress object  , which can be compared to characters with `keypress == "Q"` or to key codes with `keypress == Key.DOWN`. To get the Key class, use `from swm import Key`.