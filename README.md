# Snake Game in Pygame

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Overview
This is a modern, feature-rich Snake game built using Python and the Pygame library. The objective is to control the snake, eat food, and grow in length while avoiding collisions with the walls, yourself, and obstacles. The game now features a vibrant, modern look and icon-based food types.

---

## 🚀 Screenshots
Add your screenshots here! (Example:)

| Start Screen | Gameplay | Game Over |
|--------------|----------|-----------|
| ![Start](screenshots/start.png) | ![Game](screenshots/gameplay.png) | ![Over](screenshots/gameover.png) |

---

## 📦 Download
- [Download Windows Executable](dist/snake_game.exe) (latest build)
- Or clone and run from source (see below)

---

## Features
- Modern, vibrant UI with high-contrast colors and rounded corners
- Classic snake movement using arrow keys
- Multiple food types with unique effects and icons:
  - 🍎 **Apple (normal):** +1 length
  - ⭐ **Star (bonus):** +3 length
  - ⚡ **Lightning (speed):** +1 length, increases speed
  - 🐌 **Snail (slow):** +1 length, decreases speed
- ⬜ **Obstacles:** White blocks to avoid
- Score and high score tracking (high score is saved)
- Sound effects for eating and game over
- Pause/resume (P key)
- Start screen, game over screen, and replay option
- Custom snake/background skins (toggle with S on start screen)
- Touch-friendly: large controls and overlays
- Always uses your background image for a beautiful look

---

## 🎮 How to Play
- **Arrow Keys:** Move the snake (Up, Down, Left, Right)
- **P:** Pause/resume
- **Q:** Quit the game
- **C:** Restart after game over
- **S:** Toggle custom skins (on start screen)
- **Space:** Start the game

### Legend
| Icon | Effect |
|------|--------|
| 🍎   | Apple: +1 length |
| ⭐   | Star: +3 length |
| ⚡   | Lightning: +1 length, increases speed |
| 🐌   | Snail: +1 length, decreases speed |
| ⬜   | Obstacle: Avoid! |

---

## 🎨 Customization
- **Background:** Replace `background.jpg` with your own image for a unique look.
- **Snake Skin:** Add `snake_skin.png` for a custom snake appearance (toggle with S).
- **Sounds:** Replace `eat.wav` and `gameover.wav` for custom effects.

---

## 🛠️ Installation
To play the game on your local machine:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/adityajanjanam/pygame-snake-game.git
   cd pygame-snake-game
   ```
2. **Install Dependencies**
   ```sh
   pip install pygame
   ```
3. **Run the Game**
   ```sh
   python snake_game.py
   ```

---

## 🐍 Modern Features
- **Modern UI:** Flat, vibrant colors, rounded corners, drop shadows, and semi-transparent overlays
- **Food Icons:** Built-in shapes for food types (apple, star, lightning, snail)
- **Obstacles:** White blocks for extra challenge
- **High Score:** Saved between sessions
- **Sound:** Eating and game over effects
- **Touch-Friendly:** Large overlays and controls

---

## 📦 Deployment
- **Windows Executable:** Built with PyInstaller, available in `dist/`.
- **Other OS:** Run from source or build with PyInstaller on your OS.
- **Packaging as an executable:**
  ```sh
  pip install pyinstaller
  pyinstaller --onefile --windowed snake_game.py
  ```

---

## 🐞 Troubleshooting
- **Missing DLLs or files?** Make sure all assets (images, sounds) are in the same folder as the executable.
- **Game won’t start?** Try running from source with Python 3.7+ and Pygame installed.
- **Black screen?** Check your `background.jpg` file is present and valid.
- **Other issues?** Open an issue on GitHub!

---

## License
This project is open-source under the MIT License.

## Author
Developed by **Aditya Janjanam**

## 📫 Contact
- [LinkedIn](https://www.linkedin.com/in/adityajanjanam)
- [GitHub](https://github.com/adityajanjanam)
- [adityajanjanam.com](https://adityajanjanam.com)

For any questions or contributions, feel free to create a pull request or open an issue on GitHub!
