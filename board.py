class ChessBoard:
    def __init__(self):
        # Initialize the board as an 8x8 grid
        self.boardArray = [[' ' for _ in range(8)] for _ in range(8)]
        # Place pawns on the board
        for i in range(8):
            self.boardArray[1][i] = 'wp'  # White pawns on the second row
            self.boardArray[6][i] = 'bp'  # Black pawns on the seventh row

    def computeMove(self, move, player):
        # Implementation of move computation
        pass

    def changePerspective(self):
        # Optional: Flip the board for the opponent's perspective
        pass

    def isWin(self, player):
        # Check winning conditions
        return False
