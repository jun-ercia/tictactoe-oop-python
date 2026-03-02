""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TicTacToeGame.py

Author: Jun Y. Ercia

Description:
    Controls the overall game flow of a console-based
    Tic Tac Toe game using Object-Oriented Programming.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from board import Board
from player import Player


class TicTacToeGame:
    """
    Main controller class of the Tic Tac Toe game.
    """

    # ---------------------------------------------------------
    # Constructor Method
    # ---------------------------------------------------------
    # Purpose:
    #     Initializes the game board and two players.
    #
    # Parameters:
    #     player1_name (str) – Name of Player 1 (X)
    #     player2_name (str) – Name of Player 2 (O)
    #
    # Precondition:
    #     Both player names must be valid non-empty strings.
    #
    # Postcondition:
    #     A new game instance is created with an empty board
    #     and two initialized players.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self, player1_name: str, player2_name: str):
        self.__board = Board()
        self.__players = [
            Player(player1_name, "X"),
            Player(player2_name, "O")
        ]
        self.__current_player_index = 0


    # ---------------------------------------------------------
    # Method: start_game
    # ---------------------------------------------------------
    # Purpose:
    #     Runs the main game loop until a win or draw occurs.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Game object must be properly initialized.
    #
    # Postcondition:
    #     The game ends when a player wins or the board is full.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def start_game(self) -> None:

        while True:
            self.__board.display()
            current_player = self.__players[self.__current_player_index]

            slot_no = self.__get_valid_move(current_player)

            self.__board.place_chip(slot_no, current_player.get_chip())

            if self.__board.is_winner(current_player.get_chip()):
                self.__board.display()
                print(f"\n{current_player.get_name()} wins!")
                break

            if self.__board.is_filled():
                self.__board.display()
                print("\nGame ended in a Draw.")
                break

            self.__switch_player()


    # ---------------------------------------------------------
    # Method: __get_valid_move
    # ---------------------------------------------------------
    # Purpose:
    #     Ensures that the selected slot is available before
    #     placing a chip.
    #
    # Parameters:
    #     player (Player) – The current player object
    #
    # Precondition:
    #     Player object must exist.
    #
    # Postcondition:
    #     A valid available slot number is returned.
    #
    # Return Value:
    #     int – Valid slot number (1–9)
    # ---------------------------------------------------------
    def __get_valid_move(self, player: Player) -> int:
        while True:
            slot_no = player.move()
            if self.__board.is_available(slot_no):
                return slot_no
            else:
                print("Invalid move! Slot already taken.")


    # ---------------------------------------------------------
    # Method: __switch_player
    # ---------------------------------------------------------
    # Purpose:
    #     Switches the active player.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Current player index must be 0 or 1.
    #
    # Postcondition:
    #     Current player index is toggled.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __switch_player(self) -> None:
        self.__current_player_index = 1 - self.__current_player_index
