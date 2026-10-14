import keyboard
import time

def execute_input(user_input):
    l = user_input.split()
    i = 0

    if len(l) >= 2:
        i = 1
        hotkey = l[0].split('+')
        keyboard.press(hotkey[0])
        time.sleep(0.05)
        keyboard.write(hotkey[1])
        keyboard.release(hotkey[0])
        time.sleep(0.05)

    for char in l[i]:
        keyboard.write(char)
        if char != l[i][-1]:
            time.sleep(0.01)

