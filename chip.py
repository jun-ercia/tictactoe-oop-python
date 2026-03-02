""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
chip.py

Author: Jun Y. Ercia

Description:
    Defines the Chip class representing a player's symbol (X or O).
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Chip:
    # ---------------------------------------------------------
    # Method: __init__
    # Purpose:
    #     Initialize a chip with a symbol.
    #
    # Parameters:
    #     symbol (str): The chip symbol (e.g., "X" or "O")
    #
    # Precondition:
    #     symbol is a non-empty string.
    #
    # Postcondition:
    #     Chip is created and stores the symbol.
    #
    # Return Value:
    #     None
    # ---------------------------------------------------------
    def __init__(self, symbol: str):
        self.__symbol = symbol

    # ---------------------------------------------------------
    # Method: get_symbol
    # Purpose:
    #     Retrieve the symbol of the chip.
    #
    # Parameters:
    #     None
    #
    # Precondition:
    #     Chip is initialized.
    #
    # Postcondition:
    #     None
    #
    # Return Value:
    #     str: The chip symbol.
    # ---------------------------------------------------------
    def get_symbol(self) -> str:
        return self.__symbol
