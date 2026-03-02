""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
test_tictactoe.py

Unit tests for the Tic Tac Toe project.

Author: Jun Y. Ercia
Created: 2026

Run tests:
    python -m unittest test_tictactoe.py
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import unittest
from board import Board
from chip import Chip


class TestBoard(unittest.TestCase):
    """Test cases for Board behavior (win detection, availability, draw)."""

    def setUp(self):
        """Create a fresh board and common chips before each test."""
        self.board = Board()
        self.x_chip = Chip("X")
        self.o_chip = Chip("O")

    def test_initial_board_not_filled_and_all_slots_available(self):
        """Board should not be filled on init and all slots should be available."""
        self.assertFalse(self.board.is_filled())
        for slot_no in range(1, 10):
            self.assertTrue(self.board.is_available(slot_no), f"Slot {slot_no} should be available")

    def test_place_chip_changes_availability(self):
        """Placing a chip should make that slot unavailable."""
        self.board.place_chip(1, self.x_chip)
        self.assertFalse(self.board.is_available(1))

    def test_row_win_detection(self):
        """Horizontal (row) winning condition should be detected."""
        self.board.place_chip(1, self.x_chip)
        self.board.place_chip(2, self.x_chip)
        self.board.place_chip(3, self.x_chip)
        self.assertTrue(self.board.is_winner(self.x_chip))
        self.assertFalse(self.board.is_winner(self.o_chip))

    def test_column_win_detection(self):
        """Vertical (column) winning condition should be detected."""
        self.board.place_chip(1, self.o_chip)
        self.board.place_chip(4, self.o_chip)
        self.board.place_chip(7, self.o_chip)
        self.assertTrue(self.board.is_winner(self.o_chip))
        self.assertFalse(self.board.is_winner(self.x_chip))

    def test_main_diagonal_win_detection(self):
        """Main diagonal (1,5,9) win should be detected."""
        self.board.place_chip(1, self.x_chip)
        self.board.place_chip(5, self.x_chip)
        self.board.place_chip(9, self.x_chip)
        self.assertTrue(self.board.is_winner(self.x_chip))

    def test_secondary_diagonal_win_detection(self):
        """Secondary diagonal (3,5,7) win should be detected."""
        self.board.place_chip(3, self.o_chip)
        self.board.place_chip(5, self.o_chip)
        self.board.place_chip(7, self.o_chip)
        self.assertTrue(self.board.is_winner(self.o_chip))

    def test_partial_lines_not_winner(self):
        """Partial lines (two in a row) are not yet winners."""
        self.board.place_chip(1, self.x_chip)
        self.board.place_chip(2, self.x_chip)
        self.assertFalse(self.board.is_winner(self.x_chip))

    def test_draw_condition(self):
        """A full board with no winner should be reported as filled (draw scenario)."""
        moves = [
            (1, "X"), (2, "O"), (3, "X"),
            (4, "X"), (5, "O"), (6, "X"),
            (7, "O"), (8, "X"), (9, "O"),
        ]
        for pos, sym in moves:
            self.board.place_chip(pos, Chip(sym))

        self.assertTrue(self.board.is_filled())
        # Ensure no winner in this draw scenario (both symbols)
        self.assertFalse(self.board.is_winner(Chip("X")))
        self.assertFalse(self.board.is_winner(Chip("O")))


if __name__ == "__main__":
    unittest.main()
