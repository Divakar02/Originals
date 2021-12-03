import pyautogui
import time
import keyboard

# 161,116,56 brown

brown=(161,116,56)


def lumberbot():
    for i in range(1000):
        if keyboard.is_pressed(']'): break
        print(pyautogui.pixel(800, 511))
        if pyautogui.pixel(899,511) == brown:
            for i in range(10):
                keyboard.press_and_release("right arrow")
                time.sleep(0.1)
                if pyautogui.pixel(1032, 512) == brown:
                    break
                if keyboard.is_pressed("h"):
                    break
        else:
           keyboard.press_and_release("left arrow")
           time.sleep(0.1)




def lumberbotact():
    while True:
        if keyboard.is_pressed("["):
            lumberbot()
            break
lumberbotact()

# if pyautogui.pixel(pyautogui.position()):
#     print('HAi')


# Point(x=879, y=437)
# 175,221,127

