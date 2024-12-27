# Class that holds the blueprint for the piece object.
# The piece can be and of {rook, knight, bishop, king, queen, pawn}
class Piece():
    def __init__(self, piece):
        self.piece = piece


# ---- The following returns legal moves of a piece ---- #
    def rook_legal_moves(self) -> tuple:
        return ([], [])

    def knight_legal_moves(self) -> tuple:
        return ([], [])

    def bishop_legal_moves(self) -> tuple:
        return ([], [])

    def king_legal_moves(self) -> tuple:
        return ([], [])

    def queen_legal_moves(self) -> tuple:
        return ([], [])

    def pawn_legal_moves(self) -> tuple:
        return ([], [])
    