import random

import Comp
import Human


class Game:
    def __init__(self):
        """

        :rtype: object
        """
        self.starter = self.getStarter()
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.Computer = Comp.Comp(self)
        self.Human = Human.Human(self)
        self.ComputerWin = False

    def isWinner(self, shape):
        for i in range(3):  # בודק את האופקי
            if self.board[i][0] == shape and self.board[i][1] == shape and self.board[i][2] == shape:
                return True

        for i in range(3):  # בודק את האנכי
            if self.board[0][i] == shape and self.board[1][i] == shape and self.board[2][i] == shape:
                return True

        if self.board[0][0] == shape and self.board[1][1] == shape and self.board[2][2] == shape:  # בודק את האלכסונים
            return True
        if self.board[0][2] == shape and self.board[1][1] == shape and self.board[2][0] == shape:
            return True
        return False

    def isBoardFull(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return False
        return True

    def isGameOver(self, board):
        if self.isWinner('X') or self.isWinner('O') or self.isBoardFull(board):
            return True
        return False

    def startGame(self):

        if self.starter == 1:
            print("Computer starts")
            return self.DoingGame1()
        else:
            print("Human starts")
            return self.DoingGame2()

    def DoingGame1(self):
        boards = []
        while not self.isGameOver(self.board):
            self.ComputerTurn(boards)
            if self.isGameOver(self.board):
                break
            self.HumanTurn(boards)
            print("Boards:" + str(boards))
        if self.isWinner('X'):
            self.ComputerWin = True
        return boards, self.ComputerWin

    def DoingGame2(self):
        boards = []
        self.printBoardAsATable()
        while not self.isGameOver(self.board):
            self.HumanTurn(boards)
            if self.isGameOver(self.board):
                break
            self.ComputerTurn(boards)
            print("Boards:" + str(boards))

        if self.isWinner('O'):
            self.ComputerWin = True
        return boards, self.ComputerWin

    def ComputerTurn(self, boards):
        print("Computer's turn")
        Comp.Comp.getTurn(self.Computer, self.starter)
        boards.append(self.matrixToString())
        self.printBoardAsATable()

    def HumanTurn(self, boards):
        print("Human's turn")
        Human.Human.getTurn(self.Human, self.starter)
        boards.append(self.matrixToString())
        self.printBoardAsATable()

    def matrixToString(self):
        boardString = ""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X':
                    boardString += '1'
                elif self.board[i][j] == 'O':
                    boardString += '2'
                else:
                    boardString += '0'
        return boardString

    def getStarter(self):
        return random.randint(0, 1)

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def printBoardAsATable(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=" ")
            print()
