"""
TicTacToeGame.py

Author: Jun Y. Ercia

Description:
    Main game controller for a console-based Tic Tac Toe game.
    Orchestrates board display, player turns, move validation,
    win/draw checks, player switching, and game restart functionality.
"""

from board import Board
from player import Player


class TicTacToeGame:
    # ---------------------------------------------------------
    # Method: __init__
    # Purpose:
    #     Initialize a new Tic Tac Toe game with two players and an empty board.
    #
    # Parameters:
    #     player1_name (str): Name of Player 1 (assigned symbol "X")
    #     player2_name (str): Name of Player 2 (assigned symbol "O")
    #
    # Precondition:
    #     player1_name and player2_name are non-empty strings.
    #
    # Postcondition:
    #     Board is created, players are created, and current player index is set to 0.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self, player1_name: str, player2_name: str):
        self.__players = [
            Player(player1_name, "X"),
            Player(player2_name, "O")
        ]
        self.__board = Board()
        self.__current_player_index = 0

    # ---------------------------------------------------------
    # Method: start_game
    # Purpose:
    #     Execute the full game session. Allows replay until
    #     the user chooses to exit the program.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Game object is properly initialized.
    #
    # Postcondition:
    #     Game may restart or terminate based on user decision.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def start_game(self) -> None:
        print("\n===== TIC TAC TOE GAME STARTED =====\n")

        while True:
            self.__play_round()

            if not self.__ask_restart():
                print("\nThank you for playing Tic Tac Toe!")
                print("Program terminated successfully.\n")
                break

            self.__reset_game()

    # ---------------------------------------------------------
    # Method: __play_round
    # Purpose:
    #     Run a single round of Tic Tac Toe until win or draw.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Board and players exist.
    #
    # Postcondition:
    #     Round ends with either win or draw.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __play_round(self) -> None:
        while True:
            self.__board.display()
            current_player = self.__players[self.__current_player_index]

            slot_no = self.__get_valid_move(current_player)
            self.__board.place_chip(slot_no, current_player.get_chip())

            if self.__board.is_winner(current_player.get_chip()):
                self.__board.display()
                print(f"\nCongratulations! {current_player.get_name()} wins the game!")
                return

            if self.__board.is_filled():
                self.__board.display()
                print("\nThe game ended in a draw.")
                return

            self.__switch_player()

    # ---------------------------------------------------------
    # Method: __get_valid_move
    # Purpose:
    #     Ask the player for a move repeatedly until an available slot is chosen.
    #
    # Parameters:
    #     player (Player): The current player who will enter a move.
    #
    # Precondition:
    #     player is a valid Player object; board exists.
    #
    # Postcondition:
    #     Returns a valid slot number (1-9) that is currently available.
    #
    # Return Value:
    #     int: Available slot number.
    # ---------------------------------------------------------
    def __get_valid_move(self, player: Player) -> int:
        while True:
            slot_no = player.move()
            if self.__board.is_available(slot_no):
                return slot_no
            print("Invalid move! The selected slot is already occupied.")

    # ---------------------------------------------------------
    # Method: __switch_player
    # Purpose:
    #     Toggle the current player index between 0 and 1.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     __current_player_index is either 0 or 1.
    #
    # Postcondition:
    #     __current_player_index switches to the other player.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __switch_player(self) -> None:
        self.__current_player_index = 1 - self.__current_player_index

    # ---------------------------------------------------------
    # Method: __reset_game
    # Purpose:
    #     Reset the board and current player for a new round.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     A previous round has completed.
    #
    # Postcondition:
    #     Board is cleared and Player 1 starts again.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __reset_game(self) -> None:
        self.__board = Board()
        self.__current_player_index = 0
        print("\n===== NEW GAME STARTED =====\n")

    # ---------------------------------------------------------
    # Method: __ask_restart
    # Purpose:
    #     Ask the user whether they want to restart the game.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     A game round has ended.
    #
    # Postcondition:
    #     Returns True if user wants to restart; False otherwise.
    #
    # Return Value:
    #     bool
    # ---------------------------------------------------------
    def __ask_restart(self) -> bool:
        while True:
            choice = input("Do you want to play again? (Y/N): ").strip().upper()
            if choice == "Y":
                return True
            if choice == "N":
                return False
            print("Invalid input. Please enter 'Y' or 'N'.")
