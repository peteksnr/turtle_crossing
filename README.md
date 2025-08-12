# Turtle Crossing Game 🐢🚗

A simple **Frogger-style** game built with Python's `turtle` module. The player controls a turtle trying to cross the road while avoiding moving cars. Each time you successfully cross, the game level increases and the cars move faster.

## 🎯 Features
- **Player control** with arrow keys
- **Randomly generated cars** with varying colors
- **Increasing difficulty**: car speed increases every level
- **Score/Level tracking** displayed on screen
- **Game over** detection when a car hits the player

## 🕹️ Controls
- **Up Arrow** — Move the turtle upwards

## 📂 Project Structure
```
.
├── main.py          # Entry point: sets up the game loop and event handling
├── player.py        # Player class: movement, reset position
├── car_manager.py   # CarManager class: generates and moves cars
├── scoreboard.py    # Scoreboard class: shows current level and game over message
```
> There is no persistent high score in this game by default—score resets each run.

## 🧰 Requirements
- **Python 3.8+**
- No extra dependencies—just Python's built-in `turtle`

## 🚀 Run Locally
1. Ensure all `.py` files are in the same folder.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   .\venv\Scripts\Activate.ps1
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## ⚙️ How It Works
1. `main.py` creates the **Player**, **CarManager**, and **Scoreboard**.
2. The game loop:
   - Moves cars across the screen.
   - Randomly generates new cars.
   - Checks for **collision** with the player.
   - Detects when the player reaches the top, resets player, speeds up cars, and increments the level.
3. `player.py` handles movement and starting position.
4. `car_manager.py` handles car creation, speed increase, and movement.
5. `scoreboard.py` tracks the current level and displays "GAME OVER" on collision.

## 🎨 Customization
- **Car colors & shapes:** Edit `car_manager.py` list of colors.
- **Starting speed & speed increase:** Adjust `MOVE_INCREMENT` and `MOVE_DISTANCE` in `car_manager.py`.
- **Winning condition:** Currently reaching the top edge—can be changed in `player.py`.

## 🧪 Common Issues & Fixes
- **Turtle window doesn’t open** → Run locally in a desktop environment; `turtle` won’t work in headless servers.
- **Game runs too fast** → Increase the sleep delay in `main.py`.
- **Too few/many cars** → Adjust car generation probability in `car_manager.py`.

