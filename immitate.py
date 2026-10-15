import keyboard
import time

def execute_input(user_input):
    flag = False

    for char in user_input:
        if flag:
            time.sleep(0.05)
            keyboard.write(char)
            keyboard.release("ctrl")
            flag = False
            continue

        if char != '@':
            keyboard.write(char)
            if char != user_input[-1]:
                time.sleep(0.01)
            continue

        keyboard.press("ctrl")
        flag = True
