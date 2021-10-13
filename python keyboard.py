#https://pynput.readthedocs.io/en/latest/keyboard.html
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
# keyboard.press('a')
# keyboard.release('a')
#
# # keyboard.press(Key.cmd)
# # keyboard.release(Key.cmd)
#
# keyboard.type("This is python")

# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# keyboard.press(Key.caps_lock)
# keyboard.release(Key.caps_lock)

with keyboard.pressed(Key.cmd):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
#
#
#
