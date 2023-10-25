import json
import math

import Comp
import Game
import Human


class Games:
    def __init__(self):
        self.Dict = {}
        self.game = Game.Game()
        self.human = Human
        self.comp = Comp

    def startNewGame(self):
        self.getDictJson()
        game = self.game.startGame()
        # print(game[0])
        # print(game[1])
        if game[1]:
            self.CompWon(game)
        else:
            self.HumanWon(game)
        self.setDictJson(self.Dict)

    def HumanWon(self, game):
        for board in game[0]:
            if not board in self.Dict:
                self.Dict[board] = (0,1)
            else:
                value = self.Dict[board][0]*self.Dict[board][1]
                self.Dict[board] = value / self.Dict[board][1] + 1, self.Dict[board][1] + 1

    def CompWon(self, game):
        # print(game[0])
        game[0].reverse()
        # print(game[0])
        counter = 0
        counter2 = 1
        for board in game[0]:
            if not board in self.Dict:

                self.Dict[board] = (1 * math.pow(0.9, counter), 1)
            else:
                counter2 = self.Dict[board][1] + 1
                value = self.Dict[board][0]*self.Dict[1] + math.pow(0.9, counter)
                self.Dict[board] = (value / counter2, counter2)
            counter += 1

    # Getters
    def getGame(self):
        return self.game

    def setDictJson(self, Dict):
        with open('DicTicTacToe.json', 'w') as json_file:
            json.dump(Dict, json_file)

    def getDictJson(self):
        with open('DicTicTacToe.json', 'r') as json_file:
            self.Dict = json.loads(json_file.read())

    def getDict(self):
        return self.Dict
