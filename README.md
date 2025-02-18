# Snake Game in Pygame

## Overview
This is a simple Snake game built using Python and the Pygame library. The objective of the game is to control the snake, eat food, and grow in length while avoiding collisions with the walls and itself.

## Features
- Classic snake movement using arrow keys
- Food spawns randomly on the game board
- Score tracking
- Game over screen with replay option
- Background image for an enhanced visual experience

## Installation
To play the game on your local machine, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/adityajanjanam/pygame-snake-game.git
   cd pygame-snake-game
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then install Pygame:
   ```sh
   pip install pygame
   ```

3. **Run the Game**
   ```sh
   python main.py
   ```

## Controls
- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Q**: Quit the game
- **C**: Restart after game over

## Deployment
Since Pygame is a desktop application, deployment options include:
- **Packaging as an executable** using PyInstaller:
  ```sh
  pip install pyinstaller
  pyinstaller --onefile --windowed main.py
  ```
- **Hosting the source code** on GitHub for users to download and run locally

## License
This project is open-source under the MIT License.

## Author
Developed by **Aditya Janjanam**

For any questions or contributions, feel free to create a pull request or open an issue on GitHub!
