# Class that holds the blueprint for the piece object.
# The piece can be and of {rook, knight, bishop, king, queen, pawn}
class Piece():
    def __init__(self, piece, color):
        self.piece = piece
        self.color = color

# ---- The following returns legal moves of a piece ---- #
#   ←	↑	→	↓	↔	↕	↖	↗	↘	↙	↱
# Each returns a tuple ((moves),distance) ; if distance is -1 then distance is ∞.

    def get_legal_loves(self, piece):
        match piece:
            case "king": return self.king_legal_moves()
            case "queen": return self.queen_legal_moves()
            case "bishop": return self.bishop_legal_moves()
            case "knight": return self.knight_legal_moves()
            case "rook": return self.rook_legal_moves()
            case "pawn": return self.pawn_legal_moves()

    # helper functions

    def rook_legal_moves(self) -> tuple:
        return (('↔','↕'),-1)

    def knight_legal_moves(self) -> tuple:
        return (('↱'), 1)

    def bishop_legal_moves(self) -> tuple:
        return (('↖','↗','↘','↙'), -1)

    def king_legal_moves(self) -> tuple:
        return (('←','↑','→','↓','↖','↗','↘','↙'), 1)

    def queen_legal_moves(self) -> tuple:
        return (('←','↑','→','↓','↖','↗','↘','↙'), -1)

    def pawn_legal_moves(self) -> tuple:
        return (('↑'), 1)

# ---- The following returns the piece unicode symbol ---- #
#   ♔	♕	♗	♘   ♖	♙	♚	♛	♝	♞   ♜	♟
    def get_unicode_symbol(self) -> tuple:
        match(self.piece):
            case "king": return ('♕', '♛')[self.color == "white"]
            case "queen": return ('♔','♚')[self.color == "white"]
            case "bishop": return ('♗','♝')[self.color == "white"]
            case "knight": return ('♘','♞')[self.color == "white"]
            case "rook": return ('♖', '♜')[self.color == "white"]
            case "pawn": return ('♙','♟')[self.color == "white"]
    