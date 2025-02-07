import pyautogui
import time
import keyboard
import random

# Give the user time to move the mouse to the desired position
print("Move your mouse to the desired click location. You have 5 seconds...")
time.sleep(5)

# Get the mouse position
x, y = pyautogui.position()
print(f"Selected click position: x={x}, y={y}")

# Random offset to avoid detection
offset = 10  

print("Bot is starting! Press 'q' to stop.")

# Infinite loop, stops when 'q' is pressed
while not keyboard.is_pressed("q"):  
    rand_x = x + random.randint(-offset, offset)
    rand_y = y + random.randint(-offset, offset)
    pyautogui.click(rand_x, rand_y)
    time.sleep(random.uniform(0.02, 0.05))  # Clicks at random intervals

print("Bot stopped!")
