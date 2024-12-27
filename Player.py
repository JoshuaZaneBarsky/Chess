# Class that holds the blueprint for the player object.
from Piece import Piece

class Player():
    def __init__(self, color):
        self.color = color

        # initialize pieces
        self.king = [Piece("king")] # will only have 1 piece
        self.queen = [Piece("queen")] # will only have 1 piece
        self.rooks = [Piece("rook"), Piece("rook")]
        self.knights = [Piece("knight"), Piece("knight")]
        self.bishops = [Piece("bishop"), Piece("bishop")]
        self.pawns = [Piece("pawn"), Piece("pawn"), Piece("pawn"), Piece("pawn"), 
                      Piece("pawn"), Piece("pawn"), Piece("pawn"), Piece("pawn")]
        