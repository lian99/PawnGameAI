class ChessBoard:
    def __init__(self):
        # Initialize the board as an 8x8 grid
        self.boardArray = [[' ' for _ in range(8)] for _ in range(8)]
        self.round = 0  # Track the current round
        self.enpassant = False  # Track en passant moves
        self.enpassantCol = -1  # Track the column for en passant

    def computeMove(self, move, player):
        """
        Compute and apply a move on the board.
        :param move: The move to apply (e.g., "e2e4")
        :param player: The player making the move (0 for white, 1 for black)
        """
        # Implement pawn movement and capturing logic here
        pass

    def changePerspective(self):
        """
        Flip the board for the opponent's perspective.
        """
        self.boardArray = [row[::-1] for row in self.boardArray[::-1]]

    def isWin(self, player):
        """
        Check if the player has won.
        :param player: The player to check (0 for white, 1 for black)
        :return: True if the player has won, False otherwise
        """
        # Implement winning conditions here
        pass