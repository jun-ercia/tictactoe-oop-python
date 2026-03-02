"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
slot.py

Author: Jun Y. Ercia

Description:
    Defines a Slot class representing a single cell in the board.
    Stores a chip (or None if empty).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from chip import Chip


class Slot:
    # ---------------------------------------------------------
    # Method: __init__
    # Purpose:
    #     Initialize an empty slot.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     None
    #
    # Postcondition:
    #     Slot is created with no chip assigned.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self):
        self.__chip = None

    # ---------------------------------------------------------
    # Method: get_chip
    # Purpose:
    #     Retrieve the chip stored in this slot.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Slot is initialized.
    #
    # Postcondition:
    #     None
    #
    # Return Value:
    #     Chip | None: Chip object if occupied, otherwise None.
    # ---------------------------------------------------------
    def get_chip(self):
        return self.__chip

    # ---------------------------------------------------------
    # Method: set_chip
    # Purpose:
    #     Assign a chip to this slot.
    #
    # Parameters:
    #     chip (Chip): Chip object to place in this slot.
    #
    # Precondition:
    #     chip is a valid Chip object.
    #
    # Postcondition:
    #     Slot becomes occupied by the given chip.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def set_chip(self, chip: Chip) -> None:
        self.__chip = chip

    # ---------------------------------------------------------
    # Method: is_available
    # Purpose:
    #     Check if the slot is empty.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Slot is initialized.
    #
    # Postcondition:
    #     None
    #
    # Return Value:
    #     bool: True if empty, False if occupied.
    # ---------------------------------------------------------
    def is_available(self) -> bool:
        return self.__chip is None
