# Class that holds the blueprint for the board object.

global BOARD_SIZE
BOARD_SIZE = 8

class Board():
    def __init__(self):
        # self.board is the current board with pieces
        # self.squares is the board's squares (black and white signified by '.' and ' ')
        # self.rows is a list or row strings that will directly print
        self.board = self.squares = self.rows = []
        self.set_up_new_board()

    # Adds sets up a new game  
    def set_up_new_board(self):
        self.board = self.squares = [
            [' ' if (i + j) % 2 == 0 else '.' for j in range(8)] 
            for i in range(8)
        ]
        self.rows = []
        self.board[0] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        self.board[1] = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
        
        self.board[6] = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
        self.board[7] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']

    #--- Functions to print the board ---#
    
    def print_board_to_console(self, piece = None):
        self.update_board_with_moves(piece) # if piece == None, prints board normally
        self.print_current_board()
        self.empty_board_moves()

    # Helper Functions:
    
    # prints the board to the console
    def print_current_board(self):
        top_border = "┌" + "───┬" * (BOARD_SIZE - 1) + "───┐"
        middle_border = "├" + "───┼" * (BOARD_SIZE - 1) + "───┤"
        bottom_border = "└" + "───┴" * (BOARD_SIZE - 1) + "───┘"
        print()
        print("   A   B   C   D   E   F   G   H")
        print(" " + top_border)
        for i, row in enumerate(self.rows):
            print(str(8-i) + row)
            if i < BOARD_SIZE - 1: print(" " + middle_border)
        print(" " + bottom_border)
        print()

    # updates the board with piece moves
    def update_board_with_moves(self, piece):
        self.rows = ["│ " + (" │ ".join(row)) + " │" for row in self.board]
        if piece == None:
            return
        rows_with_moves = []
        for i in range(BOARD_SIZE):
            row_string_length = len(self.rows[i])
            moves = ""
            for j in range(row_string_length): moves += self.append_piece_moves(i,j, piece) # find where to append "▾" to row
            rows_with_moves.append(moves)
        self.rows = rows_with_moves

    # appends piece moves
    def append_piece_moves(self, i, j, piece):
        moves = ""
        if j != 0 and self.rows[i][j-1] == "│": 
            moves += self.check_if_move_is_board_legal(i,j, piece) # append "▾" or " " to row
        else: 
            moves += self.rows[i][j] # append row character as-is
        return moves
    
    def check_if_move_is_board_legal(self, i, j, piece) -> str:
        # board legal moves for (0<=i and i<=7) -->  0,1,2,...,7
        # board legal j moves are (j-1)%4==0 --> 1,5,9,13,...
        legal_moves = piece.get_legal_moves() # tuple
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == piece.get_unicode_symbol(): piece_pos = (i,(j-1)%4) # finds current pos piece name on board

        print(piece_pos)
        piece_legal_moves = piece.get_piece_current_legal_moves(piece_pos, legal_moves) # 2D list

        if piece_legal_moves[i][(j-1)%4] == 1:
            return "▾"

        # add code to compare piece_legal_moves to self.board
        # valid moves will have "▾"
        return " "

    # Emptys the board moves
    def empty_board_moves(self):
        self.rows = ["│ " + (" │ ".join(row)) + " │" for row in self.board]         
