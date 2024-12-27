# Class that holds the blueprint for the board object.
class Board():
    def __init__(self):
        # ■	□
        self.board = self.squares = [
            ['.' if (i + j) % 2 == 0 else ' ' for j in range(8)] 
            for i in range(8)
        ]
        self.add_pieces_to_board()
    
    def print_board_to_console(self):
        size = len(self.board)
        top_border = "┌" + "───┬" * (size - 1) + "───┐"
        middle_border = "├" + "───┼" * (size - 1) + "───┤"
        bottom_border = "└" + "───┴" * (size - 1) + "───┘"

        rows = ["│ " + " │ ".join(row) + " │" for row in self.board]

        print(top_border)
        for i, row in enumerate(rows):
            print(row)
            if i < size - 1:
                print(middle_border)
        print(bottom_border)


    def add_pieces_to_board(self):
        self.board[0] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        self.board[1] = ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
        
        self.board[6] = ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
        self.board[7] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']