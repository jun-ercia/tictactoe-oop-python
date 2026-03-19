# TicTacToe Game (Python)

A console-based Tic Tac Toe game implemented in Python using Object-Oriented Programming (OOP) principles, modular architecture, and unit testing.

## Features
- Two-player (X vs O) gameplay in the terminal
- Input validation (numeric only, range 1–9)
- Prevents moves on occupied slots
- Automatic win detection (rows, columns, diagonals)
- Draw detection when the board is full
- Clean OOP design with separated classes (Game, Board, Player, Slot, Chip)
- Unit test suite using `unittest`

## Project Structure

```
tictactoe-oop-python/
│── main.py
│── tictactoegame.py
│── board.py
│── player.py
│── slot.py
│── chip.py
│── test_tictactoe.py
└── README.md
```

## Requirements
- Python 3.x

## How to Run
1. Clone the repository:
   
   git clone https://github.com/<your-username>/tictactoe-oop-python.git

2. Go to the project folder:

   cd tictactoe-oop-python
   
3. Run the game:

   python main.py
   

## How to Play

* The board has 9 slots numbered from **1 to 9**:

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

* Players take turns entering a number (1–9).
* The first player to get 3 in a row wins.
* If all slots are filled and no one wins, the game ends in a draw.

## Run Unit Tests

Run the test suite with:

python -m unittest test_tictactoe.py

## OOP Design Summary

* **TicTacToeGame**: Controls the game loop, turn switching, and validations
* **Board**: Stores the 3×3 grid and checks win/draw conditions
* **Player**: Handles player identity and user input
* **Slot**: Represents one cell in the board and stores a chip
* **Chip**: Represents the player symbol (`X` or `O`)

## Author

**Jun Y. Ercia**

Faculty, Computer Science / Computer Engineering

## License

This project is provided for educational purposes. You may modify and reuse with proper credit.


