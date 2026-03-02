"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
board.py

Author: Jun Y. Ercia

Description:
    Represents a 3x3 Tic Tac Toe board and handles
    game state validation.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from slot import Slot
from chip import Chip


class Board:

    BOARD_SIZE = 3

    # ---------------------------------------------------------
    # Constructor
    # ---------------------------------------------------------
    # Purpose:
    #     Initializes a 3x3 board of empty slots.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     None
    #
    # Postcondition:
    #     Board contains 9 empty Slot objects.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self):
        self.__slots = [
            [Slot() for _ in range(self.BOARD_SIZE)]
            for _ in range(self.BOARD_SIZE)
        ]


    # ---------------------------------------------------------
    # Method: display
    # ---------------------------------------------------------
    # Purpose:
    #     Displays the current board state.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Board must be initialized.
    #
    # Postcondition:
    #     Board state is printed to console.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def display(self) -> None:
        print("\nCurrent Board:")
        for row in self.__slots:
            for col, slot in enumerate(row):
                symbol = (
                    slot.get_chip().get_symbol()
                    if not slot.is_available()
                    else "-"
                )
                print(symbol, end=" | " if col < 2 else "")
            print()


    # ---------------------------------------------------------
    # Method: place_chip
    # ---------------------------------------------------------
    # Purpose:
    #     Places a chip in the specified slot.
    #
    # Parameters:
    #     slot_no (int) – Position between 1 and 9
    #     chip (Chip) – Player chip
    #
    # Precondition:
    #     Slot must be available.
    #
    # Postcondition:
    #     Chip is assigned to the selected slot.
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
    # ---------------------------------------------------------
    # Purpose:
    #     Checks if a slot is empty.
    #
    # Parameters:
    #     slot_no (int)
    #
    # Precondition:
    #     slot_no must be between 1 and 9.
    #
    # Postcondition:
    #     Returns availability status.
    #
    # Return Value:
    #     bool – True if slot is empty
    # ---------------------------------------------------------
    def is_available(self, slot_no: int) -> bool:
        row = (slot_no - 1) // self.BOARD_SIZE
        col = (slot_no - 1) % self.BOARD_SIZE
        return self.__slots[row][col].is_available()


    # ---------------------------------------------------------
    # Method: is_filled
    # ---------------------------------------------------------
    # Purpose:
    #     Determines if all slots are occupied.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Board must be initialized.
    #
    # Postcondition:
    #     Returns whether board is full.
    #
    # Return Value:
    #     bool
    # ---------------------------------------------------------
    def is_filled(self) -> bool:
        return all(
            not slot.is_available()
            for row in self.__slots
            for slot in row
        )


    # ---------------------------------------------------------
    # Method: is_winner
    # ---------------------------------------------------------
    # Purpose:
    #     Determines if the given chip has a winning pattern.
    #
    # Parameters:
    #     chip (Chip)
    #
    # Precondition:
    #     Chip must exist.
    #
    # Postcondition:
    #     Returns True if winning condition is met.
    #
    # Return Value:
    #     bool
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

        # Diagonals
        if all(
            not self.__slots[i][i].is_available() and
            self.__slots[i][i].get_chip().get_symbol() == symbol
            for i in range(self.BOARD_SIZE)
        ):
            return True

        if all(
            not self.__slots[i][2 - i].is_available() and
            self.__slots[i][2 - i].get_chip().get_symbol() == symbol
            for i in range(self.BOARD_SIZE)
        ):
            return True

        return False
