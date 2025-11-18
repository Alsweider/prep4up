# prep4up
Python macro script to upload the latest screenshot of a game on Steam.

## Usage
1. Open the Steam desktop client.
2. Run the script from the command line, providing the name of the game as a parameter. Example:
- `cd "C:\Users\Guest\Documents\YourScriptDir"`
- `python prep4up.py "Command & Conquer"`
3. Maximise Steam.
4. The script will navigate to the Steam Screenshot Manager automatically.

Important: The x/y coordinates in the script are based on a screen resolution of 1920x1080. However, the coordinates may vary from one system to another, so adjustments might be necessary. To determine the correct coordinates for the click events, the tool [MouseInfo](https://mouseinfo.readthedocs.io/en/latest/) is recommended. 
It may also be necessary to adjust the pauses between the individual steps, as slower systems may not have the required element ready to be clicked in time.

The script assumes the following: Steam has been freshly launched and is maximised. The screenshot manager is not open. The most recent screenshot is available locally in the screenshot folder, but has not yet been uploaded.

## Requirements
- [Python](https://www.python.org) 3.10 or newer
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/) (the script will automatically install it if missing)
- [Steam client](https://store.steampowered.com/about/)
