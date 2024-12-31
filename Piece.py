# Class that holds the blueprint for the piece object.
# The piece can be and of {rook, knight, bishop, king, queen, pawn}

global BOARD_SIZE
BOARD_SIZE = 8

class Piece():
    def __init__(self, piece_name, color):
        self.piece_name = piece_name
        self.color = color

    def get_piece_name(self):
        return self.piece_name

# ---- The following returns legal moves of a piece ---- #
#   ←	↑	→	↓	↔	↕	↖	↗	↘	↙	↱
# Each returns a tuple ((moves),distance) ; if distance is -1 then distance is ∞.

    def get_legal_moves(self):
        match self.piece_name:
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
    
# ---- Gets the current legal moves for a specific piece ---- #
    def get_piece_current_legal_moves(self, piece_pos)-> list:
        current_piece_legal_moves = [[0 for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)] #2d list of zeros
        if piece_pos == None:
            return current_piece_legal_moves
        for arrow in self.get_legal_moves()[0]:
            match arrow:
                case "→": current_piece_legal_moves = self.fill_right_of_piece(piece_pos, current_piece_legal_moves)
        return current_piece_legal_moves
    
    def fill_right_of_piece(self, piece_pos, current_piece_legal_moves) -> list:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if i != piece_pos[0]:
                    pass
                if i == piece_pos[0] and j > piece_pos[1]:
                    current_piece_legal_moves[i][j] = 1
        return current_piece_legal_moves


# ---- The following returns the piece unicode symbol ---- #
#   ♔	♕	♗	♘   ♖	♙	♚	♛	♝	♞   ♜	♟
    def get_unicode_symbol(self) -> tuple:
        match(self.piece_name):
            case "king": return ('♕', '♛')[self.color == "white"]
            case "queen": return ('♔','♚')[self.color == "white"]
            case "bishop": return ('♗','♝')[self.color == "white"]
            case "knight": return ('♘','♞')[self.color == "white"]
            case "rook": return ('♖', '♜')[self.color == "white"]
            case "pawn": return ('♙','♟')[self.color == "white"]
    