import random

import Game
import Games


class Comp:
    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.getBoard()
        self.board = self.getBoard()

    def getPlace(self, num):
        if num == 0:
            return 0, 0
        if num == 1:
            return 0, 1
        if num == 2:
            return 0, 2
        if num == 3:
            return 1, 0
        if num == 4:
            return 1, 1
        if num == 5:
            return 1, 2
        if num == 6:
            return 2, 0
        if num == 7:
            return 2, 1
        if num == 8:
            return 2, 2

    def getTurn(self, starter):
        num = random.randrange(0, 9)
        if self.isFree(num):
            (i, j) = self.getPlace(num)
            if starter == 0:
                self.board[i][j] = 'O'
            else:
                self.board[i][j] = 'X'
        else:
            self.getTurn(starter)

    def setBoard(self):
        Game.Game.setBoard(self.game, self.board)

    def getBoard(self):
        return Game.Game.getBoard(self.game)

    def isFree(self,place):
        (i,j)=self.getPlace(place)
        if self.board[i][j] != 'X' and self.board[i][j] != 'O':
            return True
        return False

