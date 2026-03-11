# ☄️ Asteroids Python Game

A modern implementation of the classic **Asteroids** arcade game, built using **Python** and **Pygame**. This project is part of the **Backend Development** career path at [boot.dev](https://www.boot.dev).

Take control of a spaceship, navigate through a dangerous asteroid field, and blast your way to survival!

---

## 🚀 Features

- **Responsive Controls**: Smooth movement and rotation for precission flying.
- **Dynamic Action**: Asteroids split into smaller pieces when hit, increasing the challenge.
- **State Logging**: Real-time logging of game state and events to `jsonl` files for analysis.
- **Clean Architecture**: Built with an object-oriented approach using Pygame's Sprite system.

---

## 🎮 Controls

Navigate your ship through the cosmos using the following keys:

| Action | Key(s) |
| :--- | :--- |
| **Move Forward** | `W` |
| **Move Backward** | `S` |
| **Rotate Left** | `A` |
| **Rotate Right** | `D` |
| **Fire Laser** | `SPACE` |

---

## 🛠️ Installation & Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.

### Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended)

### Running the Game

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd asteroids-game
    ```

2.  **Install dependencies and run**:
    If you have `uv` installed:
    ```bash
    uv run main.py
    ```
    Alternatively, using standard `pip`:
    ```bash
    pip install pygame
    python3 main.py
    ```

---

## 📂 Project Structure

- `main.py`: The entry point of the game, containing the main loop and collision logic.
- `player.py`: Defines the `Player` class, handling movement, rotation, and shooting.
- `asteroid.py` & `asteroidfield.py`: Logic for asteroid behavior and spawning.
- `shot.py`: Handles the projectiles fired by the player.
- `circleshape.py`: A base class for circular game objects with collision detection.
- `constants.py`: Centralized configuration for game settings (screen size, speeds, etc.).
- `logger.py`: Utility for logging game telemetry.

---

## 📊 Telemetry

The game automatically logs its state and significant events:
- `game_state.jsonl`: Periodic snapshots of game objects.
- `game_events.jsonl`: Specific occurrences like "player hit" or "asteroid shot".

---

## 📜 License

This project is open-source and available under the MIT License.
