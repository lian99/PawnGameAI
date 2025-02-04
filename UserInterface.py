import pygame

from ai import AI


class UserInterface:
    def __init__(self, surface, board):
        """
        Initialize the user interface.
        :param surface: The Pygame surface to draw on
        :param board: The ChessBoard object representing the game state
        """
        self.surface = surface
        self.chessboard = board
        self.playerColor = 'W'  # Default to white
        self.ai = AI(board, depth=3)  # Initialize the AI

    def drawComponent(self):
        """
        Draw the game board and pieces.
        """
        # Implement the drawing logic here
        pass

    def clientMove(self):
        """
        Handle the client's move (human or AI).
        :return: The move and a flag (0 for no win/loss)
        """
        if self.playerColor == 'W':
            # Human player's turn
            move = self.getHumanMove()
        else:
            # AI's turn
            move = self.ai.getBestMove()
        return move, 0  # Return the move and a flag (0 for no win/loss)