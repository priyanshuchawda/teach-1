import pyautogui
import time
# pip install pyscreeze
#pip install Pillow --upgrade 
# #in case didnt worked go with this commands 
# python -m venv .venv  
# .venv\Scripts\activate


# Now install the packages within the virtual environment:
# pip install pyscreeze Pillow --upgrade

# --- Basic Features ---

# Get screen size
screen_width, screen_height = pyautogui.size()
print(f"Screen size: {screen_width} x {screen_height}")

# Get current mouse position
current_x, current_y = pyautogui.position()
print(f"Current mouse position: ({current_x}, {current_y})")

# Move the mouse to a specific position (x, y) over a duration (in seconds)
pyautogui.moveTo(100, 200, duration=1)  # Move to (100, 200) over 1 second

# Move the mouse relative to its current position
pyautogui.moveRel(50, -100, duration=0.5)  # Move right 50 pixels, up 100 pixels

# Click at the current mouse position (left click by default)
pyautogui.click()

# Right-click
pyautogui.click(button='right')

# Double-click
pyautogui.doubleClick()

# Click at a specific position (x, y)
pyautogui.click(x=300, y=400)

# --- Dragging ---

# Drag the mouse to a specific position (while holding down the left mouse button)
pyautogui.dragTo(500, 600, duration=1)

# Drag the mouse relative to its current position
pyautogui.dragRel(-100, 0, duration=0.5)  # Drag left 100 pixels

# --- Scrolling ---

# Scroll up 5 "clicks"
pyautogui.scroll(5)

# Scroll down 10 "clicks"
pyautogui.scroll(-10)

# --- Typing ---

# Type a string (with an optional interval between key presses in seconds)
pyautogui.typewrite("Hello, world!", interval=0.1)

# Press a specific key
pyautogui.press('enter')  # Press the Enter key
pyautogui.press('space') # Press the spacebar key

# Press a combination of keys (hotkey)
pyautogui.hotkey('ctrl', 'c')  # Copy (Ctrl+C)
pyautogui.hotkey('ctrl', 'v')  # Paste (Ctrl+V)
pyautogui.hotkey('alt','tab') # Alt+tab
# --- Screenshots ---

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()
screenshot.save("my_screenshot.png")  # Save the screenshot to a file

# Take a screenshot of a region (left, top, width, height)
region_screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))
region_screenshot.save("region_screenshot.png")

# --- Locating Images on the Screen ---

# Find the coordinates of an image on the screen (image must be on the screen)
try:
    button_location = pyautogui.locateOnScreen('button.png') #, confidence=0.8 #Optional, need opencv for confidence to work 
    if button_location:
      button_center = pyautogui.center(button_location)
      print(f"Button found at: {button_center}")
      pyautogui.click(button_center)  # Click the center of the button
    else:
      print("Button could not be found")
except Exception as e:
    print(f"Error locating image: {e}")

# --- Other ---

# Display an alert box
pyautogui.alert(text='This is an alert!', title='Alert Box', button='OK')

# Display a confirmation box (with OK and Cancel buttons)
response = pyautogui.confirm(text='Continue?', title='Confirmation', buttons=['OK', 'Cancel'])
print(f"User response: {response}")

# Display a prompt to get text input from the user
user_input = pyautogui.prompt(text='Enter your name:', title='Prompt')
print(f"User entered: {user_input}")

# --- Failsafe ---

# Move the mouse to the top-left corner of the screen (0, 0) to trigger a failsafe and stop the program
# This is useful if the program is doing something unexpected.

# --- Delays ---

# It's a good practice to add small delays (e.g., using time.sleep()) between PyAutoGUI commands
# to give the system time to process them, especially when interacting with applications.

time.sleep(2)  # Pause for 2 seconds