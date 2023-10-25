import random


class Comp:
    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.game.getBoard()
        if self.game.starter == 1:
            self.shape = 'X'
        else:
            self.shape = 'O'

    def getTurn(self):
        availableMoves = self.game.getAvailableMoves(self.board)
        if availableMoves:
            move = random.choice(availableMoves)
            self.board = self.board.replace(move, self.shape)
            self.game.setBoard(self.board)
            return self.board
class Human:
    def __init__(self, game_instance, starter):
        self.game = game_instance
        self.board = self.game.getBoard()
        if starter == 0:
            self.shape = 'X'
        else:
            self.shape = 'O'

    def getTurn(self):
        availableMoves = self.game.getAvailableBoards(self.board)
        if availableMoves:
            move = random.choice(availableMoves)
            self.board = self.board.replace(move, self.shape)
            self.game.setBoard(self.board)
            return self.board


class Game:
    def __init__(self):
        self.boards = []
        self.starter = random.randrange(0, 2)
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.Computer = Comp(self,self.starter)
        self.Human = Human(self,self.starter)
        self.ComputerWin = False

    def startGame(self):
        if self.starter == 1:
            # print("Computer starts")
            return self.CompStarts()
        else:
            # print("Human starts")
            return self.HumanStarts()

    def CompStarts(self):
        while len(self.getAvailableBoards(self.board)) > 0:
            self.Computer.getTurn()
            self.boards.append(self.board)
            if len(self.getAvailableBoards(self.board)) == 0:
                break
            self.Human.getTurn()
            self.boards.append(self.board)
        print(self.boards)

    def HumanStarts(self):
        while len(self.getAvailableBoards(self.board)) > 0:
            self.Computer.getTurn()
            self.boards.append(self.board)
            if len(self.getAvailableBoards(self.board)) == 0:
                break
            self.Human.getTurn()
            self.boards.append(self.board)
        print(self.boards)

    def getAvailableBoards(self, board):
        availableBoards = []
        for i in range(3):
            for j in range(3):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    imaginaryBoard = board
                    if self.starter == 0:
                        imaginaryBoard[i][j] = 'O'
                    else:
                        imaginaryBoard[i][j] = 'X'
                    availableBoards.append(imaginaryBoard)
        return availableBoards

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board


