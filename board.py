""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
board.py

Author: Jun Y. Ercia

Description:
    Defines the Board class which manages a 3x3 grid of Slot objects.
    Responsible for displaying the board, placing chips, and checking
    win/draw conditions.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from slot import Slot
from chip import Chip


class Board:
    BOARD_SIZE = 3

    # ---------------------------------------------------------
    # Method: __init__
    # Purpose:
    #     Create an empty 3x3 board made of Slot objects.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     None
    #
    # Postcondition:
    #     A 3x3 grid of empty Slot objects is created.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self):
        self.__slots = [[Slot() for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    # ---------------------------------------------------------
    # Method: display
    # Purpose:
    #     Print the current board state to the console.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Board is initialized.
    #
    # Postcondition:
    #     Board state is printed (X/O for occupied, '-' for empty).
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def display(self) -> None:
        print("\nCurrent Board:")
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                slot = self.__slots[row][col]
                symbol = slot.get_chip().get_symbol() if not slot.is_available() else "-"
                print(symbol, end=" | " if col < self.BOARD_SIZE - 1 else "")
            print()

    # ---------------------------------------------------------
    # Method: place_chip
    # Purpose:
    #     Place a chip into a specific board position (1–9).
    #
    # Parameters:
    #     slot_no (int): Slot number from 1 to 9.
    #     chip (Chip): Chip object containing player's symbol.
    #
    # Precondition:
    #     slot_no is between 1 and 9 AND the corresponding slot is available.
    #
    # Postcondition:
    #     The slot is updated to contain the given chip.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def place_chip(self, slot_no: int, chip: Chip) -> None:
        row = (slot_no - 1) // self.BOARD_SIZE
        col = (slot_no - 1) % self.BOARD_SIZE
        self.__slots[row][col].set_chip(chip)

    # ---------------------------------------------------------
    # Method: is_available
    # Purpose:
    #     Check whether the specified slot (1–9) is empty.
    #
    # Parameters:
    #     slot_no (int): Slot number from 1 to 9.
    #
    # Precondition:
    #     slot_no is between 1 and 9.
    #
    # Postcondition:
    #     None (board state not modified).
    #
    # Return Value:
    #     bool: True if slot is empty; False otherwise.
    # ---------------------------------------------------------
    def is_available(self, slot_no: int) -> bool:
        row = (slot_no - 1) // self.BOARD_SIZE
        col = (slot_no - 1) % self.BOARD_SIZE
        return self.__slots[row][col].is_available()

    # ---------------------------------------------------------
    # Method: is_filled
    # Purpose:
    #     Determine whether all slots on the board are occupied.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Board is initialized.
    #
    # Postcondition:
    #     None (board state not modified).
    #
    # Return Value:
    #     bool: True if board is full; False otherwise.
    # ---------------------------------------------------------
    def is_filled(self) -> bool:
        return all(not slot.is_available() for row in self.__slots for slot in row)

    # ---------------------------------------------------------
    # Method: is_winner
    # Purpose:
    #     Check if the given chip has formed a winning pattern
    #     (3 in a row, column, or diagonal).
    #
    # Parameters:
    #     chip (Chip): Chip object for the player being checked.
    #
    # Precondition:
    #     chip is a valid Chip object.
    #
    # Postcondition:
    #     None (board state not modified).
    #
    # Return Value:
    #     bool: True if the chip has a winning line; False otherwise.
    # ---------------------------------------------------------
    def is_winner(self, chip: Chip) -> bool:
        symbol = chip.get_symbol()

        # Check rows
        for row in self.__slots:
            if all(not s.is_available() and s.get_chip().get_symbol() == symbol for s in row):
                return True

        # Check columns
        for col in range(self.BOARD_SIZE):
            if all(
                not self.__slots[row][col].is_available() and
                self.__slots[row][col].get_chip().get_symbol() == symbol
                for row in range(self.BOARD_SIZE)
            ):
                return True

        # Check main diagonal
        if all(
            not self.__slots[i][i].is_available() and
            self.__slots[i][i].get_chip().get_symbol() == symbol
            for i in range(self.BOARD_SIZE)
        ):
            return True

        # Check secondary diagonal
        if all(
            not self.__slots[i][self.BOARD_SIZE - 1 - i].is_available() and
            self.__slots[i][self.BOARD_SIZE - 1 - i].get_chip().get_symbol() == symbol
            for i in range(self.BOARD_SIZE)
        ):
            return True

        return False
