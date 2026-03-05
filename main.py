"""
File Name: main.py
Program: Tic-Tac-Toe Game (Object-Oriented Programming Version)

Author: Jun Y. Ercia
Date Written: March 4, 2026

Description:
This file serves as the entry point of the Tic-Tac-Toe application.
It initializes the TicTacToeGame object and starts the game loop.

Responsibilities of this file:
- Import the main game controller class (TicTacToeGame)
- Provide player names
- Create a game instance
- Start the game

Note:
All core game logic such as board management, player turns,
move validation, win/draw checking, and board display are
handled inside the TicTacToeGame class and its related classes
(Board, Player, Slot, and Chip).
"""

# Import the main game controller class
from TicTacToeGame import TicTacToeGame


def main():
    """
    Precondition:
    - TicTacToeGame class must be available and successfully imported.
    - Player names must be valid non-empty strings.

    Postcondition:
    - The Tic-Tac-Toe game starts and continues until a player wins
      or the game results in a draw.
    """

    # Initialize the game with two player names
    player1_name = "Paul Allen"
    player2_name = "Mitz"

    # Create a new TicTacToeGame object
    game = TicTacToeGame(player1_name, player2_name)

    # Start the game loop
    game.start_game()


# Execute the main function only when this file is run directly
if __name__ == "__main__":
    main()
