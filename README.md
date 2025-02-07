# Auto Clicker Bot

## Overview
This is an **automatic mouse clicker bot** written in Python. It clicks at a specified position repeatedly until stopped by the user. The bot includes **randomized movement and click delays** to help avoid detection by anti-bot systems.

## Features
- **Automatic clicking** at a selected position
- **Randomized movement** to avoid detection
- **Customizable click speed**
- **Easy start & stop** using the `ESC` key
- **Standalone `.exe` version** for computers without Python

## Installation
### 1️⃣ Install Python and Required Libraries
If running the script directly (`.py` file), install Python and dependencies:

```bash
pip install pyautogui keyboard pynput
```

### 2️⃣ Convert to .exe (Optional)
To run the bot on another computer **without Python installation**, convert it to a `.exe` file using:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole auto_clicker.py
```

The executable will be in the `dist/` folder as `auto_clicker.exe`.

## Usage
### Running the Script (`.py` version)
```bash
python auto_clicker.py
```
1. Move your mouse to the **desired click position** within **5 seconds**.
2. The bot will start clicking automatically.
3. Press `ESC` to stop the bot.

### Running the Executable (`.exe` version)
1. **Double-click `auto_clicker.exe`**
2. Move the mouse to the target position within **5 seconds**.
3. The bot will start clicking.
4. **Press `ESC` to stop**.

## Customization
Modify `auto_clicker.py` to adjust click speed:
```python
time.sleep(random.uniform(0.02, 0.05))  # Adjust for faster or slower clicking
```

## Notes
- Some games or applications may block automated clicks.
- Use at your own risk. Make sure to comply with the terms of service of the game/software you use it on.

## License
This project is released under the **MIT License**. You are free to modify and distribute it.

---
**Happy Clicking! 🚀**

