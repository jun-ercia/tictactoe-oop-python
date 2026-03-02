"""
player.py

Author: Jun Y. Ercia

Description:
    Defines the Player class. Stores player details and handles
    user input with validation.
"""

from chip import Chip


class Player:
    # ---------------------------------------------------------
    # Method: __init__
    # Purpose:
    #     Initialize a player with a name and a chip symbol.
    #
    # Parameters:
    #     name (str): Player name
    #     symbol (str): Player symbol (e.g., "X" or "O")
    #
    # Precondition:
    #     name is a non-empty string; symbol is a valid single-character string.
    #
    # Postcondition:
    #     Player is created with a Chip object assigned.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self, name: str, symbol: str):
        self.__name = name
        self.__chip = Chip(symbol)

    # ---------------------------------------------------------
    # Method: get_name
    # Purpose:
    #     Retrieve the player's name.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Player object is initialized.
    #
    # Postcondition:
    #     None
    #
    # Return Value:
    #     str: Player name
    # ---------------------------------------------------------
    def get_name(self) -> str:
        return self.__name

    # ---------------------------------------------------------
    # Method: get_chip
    # Purpose:
    #     Retrieve the player's chip object.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Player object is initialized.
    #
    # Postcondition:
    #     None
    #
    # Return Value:
    #     Chip: Player's chip
    # ---------------------------------------------------------
    def get_chip(self) -> Chip:
        return self.__chip

    # ---------------------------------------------------------
    # Method: move
    # Purpose:
    #     Prompt the player to enter a move (slot number 1-9)
    #     and validate it as an integer within range.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Console input is available.
    #
    # Postcondition:
    #     Returns a valid integer between 1 and 9.
    #
    # Return Value:
    #     int: Slot number (1-9)
    # ---------------------------------------------------------
    def move(self) -> int:
        while True:
            try:
                slot_no = int(input(f"{self.__name}, Enter your move (1-9): "))
                assert 1 <= slot_no <= 9, "Invalid Move! Move should be between 1 and 9."
                return slot_no
            except ValueError:
                print("Invalid Move! Not a number.")
            except AssertionError as ae:
                print(ae)
