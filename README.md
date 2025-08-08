# ShooterGame

/!\ This project is an old project /!\

**A small Python shooter game** built with an **OOP approach**. Inspired by Graven’s tutorial (link below).

---

## Main Features

* **Player movement**, **projectile shooting**, and **collision detection** with enemies
* Basic enemy AI behavior
* **Game loop management** (update, render, game state handling)
* **Modular code structure** (`player.py`, `monster.py`, etc.)
* Easy configuration via `constant.py` (window size, speeds, colors, etc.)

---

## Installation & Run

1. Clone the repository:

   ```bash
   git clone https://github.com/0Blanck0/ShooterGame.git
   cd ShooterGame
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the game:

   ```bash
   python main.py
   ```

---

## Project Structure

* `main.py` — entry point and main game loop
* `game.py` — core game logic (states, updates, rendering)
* `player.py` — player behavior and mechanics
* `monster.py` — enemy behavior and mechanics
* `bullet.py` — projectile logic
* `constant.py` — configuration (sizes, colors, speeds...)
* `requirements.txt` — dependencies (e.g., Pygame)

---

## Original Tutorial

This project follows the **Graven** YouTube tutorial, serving as an ideal starting point for learning or building your own shoot-’em-up:

> \[Graven Tutorial Link]
> ([github.com](https://github.com/0Blanck0/ShooterGame))

---

## How to Contribute / Extend

1. **Fork** the repository and make your changes
2. Improve modularity or readability (tests, documentation, etc.)
3. Add new features (score system, power-ups, levels, animations, etc.)
4. Submit a **pull request** with:

   * A clear title
   * An explanation of changes
   * Testing details for new features

---


## Summary

* Fully functional Python shooter
* Clear and organized codebase
* Documentation to get you started right away


