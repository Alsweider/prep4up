import sys
import subprocess
import importlib
import time

#Check required modules
required_modules = ["pyautogui"]

for module in required_modules:
    try:
        importlib.import_module(module)
    except ImportError:
        print(f"Modul '{module}' missing, will be installed...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        print(f"Modul '{module}' installed successfully.")

# Import modul now
import pyautogui


# Parameter
if len(sys.argv) < 2:
    print("Please provide the game name as a parameter!")
    sys.exit(1)

game_name = sys.argv[1]

# Time to react
print("Please activate and maximise the Steam window. You have 5 seconds...")
time.sleep(5)

# Step 1: Click "View"
pyautogui.click(111, 18)
time.sleep(1)

# Step 2: Click Recordings & Screenshots
pyautogui.click(180, 415)
time.sleep(1)

# Step 3: Maximise screenshot manager (Doubleclick on upper edge of the window. Skip this if it already is max.)
pyautogui.doubleClick(890, 21)
time.sleep(1)

# Step 4: Open game list
pyautogui.click(231, 75)
time.sleep(1)

#Step 5: Click on search field
pyautogui.click(231, 131)
time.sleep(1)

# Step 6: Enter name of your game (until 2nd space, each additional character will abort search)
space_count = 0
partial_name = ""

for char in game_name:
    partial_name += char
    if char == " ":
        space_count += 1
    if space_count == 2:
        break

pyautogui.write(partial_name, interval=0.05)
time.sleep(1)

# Step 7: Click on 1st search result
pyautogui.click(231, 160)
time.sleep(1)

# Step 8: Click on 1st screenshot
pyautogui.click(231, 160)
time.sleep(1)

# Step 9: Click Share
pyautogui.click(1856, 993)
time.sleep(1)

# Step 10: Click Share on Steam 
pyautogui.click(1767, 723)
time.sleep(1)

#Done
print("I trust you are capable of pressing the final button with your own hands.")
