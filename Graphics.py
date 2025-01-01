# Will be the main file for graphics once Game.py is complete
from Game import Game


def run():
    game = Game()
    king = game.black.king[0]
    game.board.print_board_to_console(king)

run()