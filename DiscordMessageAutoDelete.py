import time
from pynput.keyboard import Key, Controller

def autoMessageDelete(limit:int=5):
    # Initializing the Controller
    control = Controller()

    time.sleep(8)

    for l in range(0,limit):
        # Pressing the Up Arrow Key
        control.press(Key.up)
        control.release(Key.up)

        time.sleep(0.5)

        # Pressing ctrl + a
        with control.pressed(Key.ctrl):
            control.press("a")
            control.release("a")
        
        # Pressing the Backspace Key
        control.press(Key.backspace)
        control.release(Key.backspace)

        # Pressing the Enter Key
        control.press(Key.enter)
        control.release(Key.enter)

        time.sleep(0.5)

        # Pressing the Enter Key
        control.press(Key.enter)
        control.release(Key.enter)

        time.sleep(0.5)

        # Typing something
        control.type("x")
        time.sleep(0.2)
        control.press(Key.backspace)
        control.release(Key.backspace)
        time.sleep(0.5)


# Running the Function
if __name__ == "__main__":
    limit= int(input("Enter the number of messages you want to delete: "))
    autoMessageDelete(limit=limit)
