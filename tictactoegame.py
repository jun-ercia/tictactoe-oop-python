"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
TicTacToeGame.py

Author: Jun Y. Ercia

Description:
    Main game controller for a console-based Tic Tac Toe game.
    Orchestrates board display, player turns, move validation,
    win/draw checks, and player switching.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
        self.__board = Board()
        self.__players = [Player(player1_name, "X"), Player(player2_name, "O")]
        self.__current_player_index = 0

    # ---------------------------------------------------------
    # Method: start_game
    # Purpose:
    #     Run the main game loop until a player wins or the game ends in a draw.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Game object is initialized; board and players exist.
    #
    # Postcondition:
    #     Game ends after win or draw; final board state and result printed.
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
    #     Returns a valid slot number (1-9) that is currently available on the board.
    #
    # Return Value:
    #     int: An available slot number from 1 to 9.
    # ---------------------------------------------------------
    def __get_valid_move(self, player: Player) -> int:
        while True:
            slot_no = player.move()
            if self.__board.is_available(slot_no):
                return slot_no
            print("Invalid move! Slot already taken.")

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
    #     __current_player_index is switched to the other player.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __switch_player(self) -> None:
        self.__current_player_index = 1 - self.__current_player_index
