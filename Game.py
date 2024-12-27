# Class that holds the blueprint for the player object.
from Player import Player
from Board import Board

class Game():
    def __init__(self):
        self.black = Player("black")
        self.white = Player("white")
        self.board = Board()