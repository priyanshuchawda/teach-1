import pyautogui
from PIL import ImageGrab
import tkinter as tk

def on_button_click(choice):
    print(f"User clicked {choice}")
    root.destroy()  


root = tk.Tk()
root.title("Custom Alert Box")


label = tk.Label(root, text="Do you want to proceed?")
label.pack(pady=10)


button_proceed = tk.Button(root, text="Yes", command=lambda: on_button_click("Proceed"))
button_proceed.pack(side=tk.LEFT, padx=10)

button_abort = tk.Button(root, text="No opetion you need to", command=lambda: on_button_click("Abort"))
button_abort.pack(side=tk.LEFT, padx=10)

button_ignore = tk.Button(root, text="Cant stop it", command=lambda: on_button_click("Ignore"))
button_ignore.pack(side=tk.LEFT, padx=10)


root.mainloop()
pyautogui.moveTo(1000, 200, duration=1) 
pyautogui.click()



screenshot = ImageGrab.grab()
screenshot.save('screenshot.png')
print("Screenshot saved successfully!")


pyautogui.alert('Cant do anything now')
pyautogui.alert('Got your computer in my hand')
