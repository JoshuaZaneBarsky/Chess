# Will be the main file for graphics once Game.py is complete
from Game import Game


def run():
    game = Game()
    queen = game.white.queen[0]
    game.board.print_board_to_console(queen)

run()