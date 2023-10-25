import copy
import json
import random

import Game


class Comp:
    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.getBoard()
        self.Dict = {}def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.getBoard()
        self.Dict = {}

    def getDictJson(self):
        with open('DicTicTacToe.json', 'r') as json_file:
            self.Dict = json.loads(json_file.read())



    def getAvailableMoves(self):
        availableMoves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 'X' and self.board[i][j] != 'O':
                    availableMoves.append((i, j))
        return availableMoves

    def getAvailableBoards(self,starter):
        availableBoards = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 'X' and self.board[i][j] != 'O':
                    imaginaryBoard = copy.deepcopy(self.board)
                    if starter == 0:
                        imaginaryBoard[i][j] = 'O'
                    else:
                        imaginaryBoard[i][j] = 'X'
                    availableBoards.append(self.matrixToString(imaginaryBoard))
        return availableBoards

    def getRandomTurn(self, starter):
        self.getDictJson()
        availableMoves = self.getAvailableMoves()
        if availableMoves:
            move = random.choice(availableMoves)
            (i, j) = move
            if starter == 0:
                self.board[i][j] = 'O'
            else:
                self.board[i][j] = 'X'
            return self.board


    def getBestMove(self, starter):
        self.getDictJson()
        availableBoards = self.getAvailableBoards(starter)
        bestBoard = ""
        bestValue = 0
        if availableBoards:
            bestBoard = availableBoards[0]
            # print(bestBoard)
            if bestBoard in self.Dict:
                bestValue = self.Dict[bestBoard]
            for board in availableBoards:
                if board in self.Dict and self.Dict[board] > bestValue:
                    bestBoard = board
                    bestValue = self.Dict[board]
            newBoard = self.stringToMatrix(bestBoard)
            # print(newBoard)
            # print(bestValue)
            return newBoard


    def setBoard(self):
        Game.Game.setBoard(self.game, self.board)

    def getBoard(self):
        return Game.Game.getBoard(self.game)



    def matrixToString(self, board):
        boardString = ""
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    boardString += '1'
                elif board[i][j] == 'O':
                    boardString += '2'
                else:
                    boardString += '0'
        return boardString

    def stringToMatrix(self, boardString):
        board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        for i in range(3):
            for j in range(3):
                if boardString[i * 3 + j] == '1':
                    board[i][j] = 'X'
                elif boardString[i * 3 + j] == '2':
                    board[i][j] = 'O'
        return board


