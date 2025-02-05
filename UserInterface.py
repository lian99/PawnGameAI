import pygame
from ai import AI

# Constants
WINDOW_SIZE = 600
SQUARE_SIZE = WINDOW_SIZE // 8
LIGHT_GRAY = (240, 217, 181)  # Natural light square color
DARK_GRAY = (181, 136, 99)    # Natural dark square color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (34, 139, 34)  # Forest green for better visibility on both light and dark squares
FONT_SIZE = 24

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
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)
        self.time_remaining = 300  # 5 minutes per player (in seconds)
        self.selected_pawn = None  # Track the selected pawn for movement
        self.legal_moves = []  # Track legal moves for the selected pawn

    def drawComponent(self):
        """
        Draw the game board and pieces.
        """
        self.surface.fill(WHITE)  # Clear the screen

        # Draw the chessboard
        for row in range(8):
            for col in range(8):
                color = LIGHT_GRAY if (row + col) % 2 == 0 else DARK_GRAY
                pygame.draw.rect(self.surface, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                # Highlight legal moves
                if self.selected_pawn and (row, col) in self.legal_moves:
                    pygame.draw.rect(self.surface, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

                # Draw the pawns
                piece = self.chessboard.boardArray[row][col]
                center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                if piece == 'wp':  # White pawn
                    pygame.draw.circle(self.surface, WHITE, (center_x, center_y), SQUARE_SIZE // 3)
                elif piece == 'bp':  # Black pawn
                    pygame.draw.circle(self.surface, BLACK, (center_x, center_y), SQUARE_SIZE // 3)

        # Draw the timer
        timer_text = self.font.render(f"Time: {self.time_remaining // 60}:{self.time_remaining % 60:02}", True, RED)
        self.surface.blit(timer_text, (10, 10))

        pygame.display.flip()  # Update the display

    def updateTimer(self, time_remaining):
        """
        Update the timer for the current player.
        :param time_remaining: The remaining time in seconds
        """
        self.time_remaining = time_remaining
        self.drawComponent()  # Redraw the UI to update the timer
