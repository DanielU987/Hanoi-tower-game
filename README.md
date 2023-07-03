# Hanoi Tower Game in Python

## Introduction
This is a simple implementation of the Hanoi Tower game in Python. The game involves moving disks from one tower to another, following specific rules, to achieve the objective of transferring all the disks to a different tower. The game provides a console-based interface for the user to interact and play.

## Rules of the Game
The Hanoi Tower game follows the following rules:
- The game consists of three towers (0, 1, and 2) and a number of disks of different sizes.
- The disks are initially stacked in decreasing order of size on one tower (e.g., tower 0), with the largest disk at the bottom.
- The objective is to move all the disks to another tower (e.g., tower 2), following these rules:
  1. Only one disk can be moved at a time.
  2. Each move consists of taking the top disk from one of the towers and placing it on top of another tower.
  3. No disk may be placed on top of a smaller disk.

## Getting Started
To play the Hanoi Tower game, follow these steps:

1. Clone the repository from GitHub:

```shell
git clone https://github.com/your-username/hanoi-tower-game.git
```
2. Open a command prompt or terminal and navigate to the project directory.
3. Run the following command to start the game:
```shell
python Hanoi.py
```
4. Follow the on-screen instructions to play the game.
5. Enjoy playing the Hanoi Tower game!

## How to Play
- The game displays the current state of the towers, represented by letters (0, 1, and 2) and disks (numbers).
- To make a move, enter the source tower and the destination tower as prompted.
- The game validates each move and displays an error message if an invalid move is attempted.
- Keep making moves until you successfully transfer all the disks to a different tower.
- The game will display a congratulatory message upon winning the game.

## Customization
- You can modify the number of disks in the `Hanoi.py` file by updating the number list.
- Feel free to customize the game's interface or add additional features to enhance the gameplay.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## Acknowledgments
This project was inspired by the classic Hanoi Tower puzzle and built using Python.

## Contact
Have fun playing the Hanoi Tower game and challenge yourself with the puzzle!
