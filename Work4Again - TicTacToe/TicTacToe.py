import json
import math
import random


class Comp:
    def load_dict_from_json(self):
        with open('Dict.json', 'r') as json_file:
            return json.load(json_file, object_hook=lambda item: {k: tuple(v) for k, v in item.items()})

    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.game.getBoard()
        self.shape = 'X' if self.game.getStarter() == 1 else 'O'
        self.Dict = self.load_dict_from_json()

    # def getTurn(self):
    #     self.board = self.game.getBoard()
    #     availableBoards = self.game.getAvailableBoards(self.board, self.shape)
    #     if availableBoards:
    #         board = random.choice(availableBoards)
    #         self.board = board
    #         self.game.setBoard(board)
    #         return self.board
    def getTurn(self):

        board = self.getBestTurn()
        self.board = board
        self.game.setBoard(board)
        return self.board

    def getBestTurn(self):
        self.board = self.game.getBoard()
        availableBoards = self.game.getAvailableBoards(self.board, self.shape)
        maxBoard = 0
        bestBoard = availableBoards[0]

        if availableBoards:
            for board in availableBoards:

                realBoard = self.game.convertToNormalStringForBoards(board)
                if realBoard in self.Dict:

                    if self.Dict[realBoard][0] > maxBoard:
                        bestBoard = board
                        maxBoard = self.Dict[realBoard][0]
        return bestBoard


class Human:
    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.game.getBoard()
        self.shape = 'X' if self.game.getStarter() == 0 else 'O'

    def getTurn(self):
        self.board = self.game.getBoard()
        availableBoards = self.game.getAvailableBoards(self.board, self.shape)
        if availableBoards:
            board = random.choice(availableBoards)
            self.board = board
            self.game.setBoard(board)
            return self.board


class Game:
    def __init__(self):
        self.boards = []
        self.starter = random.randrange(0, 2)
        # print(self.starter)
        self.board = '123456789'
        self.Computer = Comp(self)
        self.Human = Human(self)
        self.ComputerWin = False

    def startGame(self):
        if self.starter == 1:
            # print("Computer starts")
            return self.CompStarts()
        else:
            # print("Human starts")
            return self.HumanStarts()

    def CompStarts(self):
        while not self.isGameOver():
            # print("Computer Turn")
            self.Computer.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            # self.printableBoard(self.board)
            if self.isGameOver():
                break
            # print("Human Turn")
            self.Human.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            # self.printableBoard(self.board)
        if self.isWinner('X'):
            self.ComputerWin = True
        return self.boards, self.ComputerWin

    def HumanStarts(self):
        while not self.isGameOver():
            # print("Human Turn")
            self.Human.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            # self.printableBoard(self.board)
            if self.isGameOver():
                break
            # print("Computer Turn")
            self.Computer.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            # self.printableBoard(self.board)
        if self.isWinner('O'):
            self.ComputerWin = True
        return self.boards, self.ComputerWin

    def getAvailableBoards(self, board, shape='X'):
        availableBoards = []
        for i in range(9):
            if board[i] != 'X' and board[i] != 'O':
                imaginaryBoard = board[:i] + shape + board[i + 1:]
                availableBoards.append(imaginaryBoard)
        # print(availableBoards)
        return availableBoards

    def printableBoard(self, board):
        for i in range(0, 9, 3):
            print(board[i], board[i + 1], board[i + 2])

    def isWinner(self, shape):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in win_combinations:
            if all(self.board[i] == shape for i in combo):
                return True
        return False

    def isDraw(self):
        for i in self.board:
            if i != 'X' and i != 'O':
                return False
        return True

    def isGameOver(self):
        return self.isWinner('X') or self.isWinner('O') or self.isDraw()

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getStarter(self):
        return self.starter

    def convertToNormalStringForBoards(self, board):
        normal_board = ''
        if self.starter == 1:
            for cell in board:
                if cell == 'X':
                    normal_board += '2'
                elif cell == 'O':
                    normal_board += '1'
                else:
                    normal_board += '0'
        else:
            for cell in board:
                if cell == 'X':
                    normal_board += '1'
                elif cell == 'O':
                    normal_board += '2'
                else:
                    normal_board += '0'
        return normal_board


class Games:
    def load_dict_from_json(self):
        with open('Dict.json', 'r') as json_file:
            return json.load(json_file, object_hook=lambda item: {k: tuple(v) for k, v in item.items()})

    def save_dict_to_json(self, Dict):
        with open('Dict.json', 'w') as json_file:
            json.dump(Dict, json_file, default=lambda item: {k: list(v) for k, v in item.items()})

    def __init__(self):
        self.Dict = self.load_dict_from_json()

    def startGame(self):
        self.Dict = self.load_dict_from_json()
        game = Game()
        boards, compWon = game.startGame()
        # print(boards)
        # print(compWon)
        boards.reverse()
        self.DictionaryUpdating(boards, compWon)
        # print(self.Dict)
        self.save_dict_to_json(self.Dict)
        return compWon

    def DictionaryUpdating(self, boards, compWon):
        counter = 0
        for board in boards:
            if board in self.Dict:
                if compWon:
                    currentValue = self.Dict[board][0]
                    currentTimes = self.Dict[board][1]
                    self.Dict[board] = tuple(
                        (((currentValue * currentTimes) + math.pow(0.9, counter)) / (currentTimes + 1),
                         (currentTimes + 1)))
                    # print("Current Value: ", currentValue)
                    # print(self.Dict[board])
                    # print(counter)
                else:
                    currentValue = self.Dict[board][0]
                    currentTimes = self.Dict[board][1]
                    self.Dict[board] = tuple(((currentValue * currentTimes) / (currentTimes + 1), currentTimes + 1))
            else:
                if compWon:
                    self.Dict[board] = tuple((math.pow(0.9, counter), 1))
                else:
                    self.Dict[board] = tuple((0, 1))
            counter += 1


if __name__ == '__main__':
    counter = 0
    games = Games()
    for i in range(100000):
        print(i)
        if games.startGame():
            counter += 1
    print(counter)


