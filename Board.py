# Class that holds the blueprint for the board object.
class Board():
    def __init__(self):
        # self.board is the current playing board
        # self.squares is the board's squares (black and white signified by '.' and ' ')
        self.board = self.squares = [
            [' ' if (i + j) % 2 == 0 else '.' for j in range(8)] 
            for i in range(8)
        ]
        self.add_pieces_to_board()
    
    def print_board_to_console(self):
        size = len(self.board)
        top_border = "┌" + "───┬" * (size - 1) + "───┐"
        middle_border = "├" + "───┼" * (size - 1) + "───┤"
        bottom_border = "└" + "───┴" * (size - 1) + "───┘"

        rows = ["│ " + (" │ ".join(row)) + " │" for row in self.board]

        # edits rows based on moves
        rows_with_moves = []
        for i in range(size):
            moves = ""
            for j in range(len(rows[i])):
                if j != 0 and rows[i][j-1] == "│":
                    moves += "▾"
                else:
                    moves += rows[i][j]
            rows_with_moves.append(moves)   # last edited - now to adjust when a square gets a triangle (possible move for a piece)

        for i in range(len(rows_with_moves)):
            print(rows_with_moves[i])         
        

        # prints the board to the console
        print()
        print("   A   B   C   D   E   F   G   H")
        print(" " + top_border)
        for i, row in enumerate(rows):
            print(str(8-i) + row)
            if i < size - 1:
                print(" " + middle_border)
        print(" " + bottom_border)
        print()


    def add_pieces_to_board(self):
        self.board[0] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        self.board[1] = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
        
        self.board[6] = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
        self.board[7] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']