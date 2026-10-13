import keyboard
import time

def execute_input(user_input):
    parts = user_input.split()
    
    for part in parts:
        if '+' in part or part.lower() in ['enter', 'backspace', 'tab', 'space']:
            print(f"Натискаю хоткей: {part}")
            keyboard.send(part.lower())
        else:
            print(f"Друкую текст: {part}")
            keyboard.write(part + " ")
            
        time.sleep(0.05)

