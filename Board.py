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
        self.set_up_board_moves(piece)
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

    #  edits rows based on moves
    def set_up_board_moves(self, piece): # piece will show the possible board moves for any piece (optional parameter)
        self.rows = ["│ " + (" │ ".join(row)) + " │" for row in self.board]
        if piece == None:
            return
        size = len(self.board)
        self.update_board_with_moves(piece)

    def update_board_with_moves(self, piece):
        if piece == None:
            return
        rows_with_moves = []
        for i in range(BOARD_SIZE):
            moves = ""
            for j in range(len(self.rows[i])): moves += self.append_piece_moves(i,j, piece)
            rows_with_moves.append(moves)
        self.rows = rows_with_moves

    def append_piece_moves(self, i, j, moves):
        if j != 0 and self.rows[i][j-1] == "│": 
            moves += "▾"
        else: 
            moves += self.rows[i][j]
        return moves

    # Emptys the board moves
    def empty_board_moves(self):
        self.rows = ["│ " + (" │ ".join(row)) + " │" for row in self.board]         
