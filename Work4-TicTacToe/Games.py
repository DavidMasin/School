import Comp
import Game
import Human


class Games:
    def __init__(self):
        self.game = Game.Game()
        self.human = Human
        self.comp = Comp


    def getGame(self):
        return self.game

    def startNewGame(self):
        game = self.game.startGame()
        print(game)


