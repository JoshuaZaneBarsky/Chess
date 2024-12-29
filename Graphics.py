# Will be the main file for graphics once Game.py is complete
from Game import Game


def run():
    game = Game()
    king_moves = game.black.king[0].get_legal_moves()
    king = game.black.king[0]
    game.board.print_board_to_console(king)

run()