# Will be the main file for graphics once Game.py is complete
from Game import Game


def run():
    game = Game()
    game.board.print_board_to_console()

run()