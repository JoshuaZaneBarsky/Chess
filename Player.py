# Class that holds the blueprint for the player object.
from Piece import Piece

class Player():
    def __init__(self, color):
        self.color = color

        # initialize pieces
        self.king = [Piece("king", self.color)] # will only have 1 piece
        self.queen = [Piece("queen", self.color)] # will only have 1 piece
        self.rooks = [Piece("rook", self.color), Piece("rook", self.color)]
        self.knights = [Piece("knight", self.color), Piece("knight", self.color)]
        self.bishops = [Piece("bishop", self.color), Piece("bishop", self.color)]
        self.pawns = [Piece("pawn", self.color), Piece("pawn", self.color), Piece("pawn", self.color), Piece("pawn", self.color), 
                      Piece("pawn", self.color), Piece("pawn", self.color), Piece("pawn", self.color), Piece("pawn", self.color)]
        