import json
import math
import random

import kivy.uix.button
import numpy as np

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Comp:
    def load_dict_from_json(self):
        with open('Dict.json', 'r') as json_file:
            # Use a custom decoding function to preserve the tuple data type
            return json.load(json_file, object_hook=lambda item: {k: tuple(v) for k, v in item.items()})

    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.game.getBoard()
        if self.game.getStarter() == 1:
            self.shape = 'X'
        else:
            self.shape = 'O'
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
                if board in self.Dict:
                    if self.game.Dict[board][0] > maxBoard:
                        bestBoard = board
                        maxBoard = self.game.Dict[board][0]
        return bestBoard


class Human:
    def __init__(self, game_instance):
        self.game = game_instance
        self.board = self.game.getBoard()
        self.starter = self.game.getStarter()
        if self.starter == 0:
            self.shape = 'X'
        else:
            self.shape = 'O'

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
        self.board = '123456789'  # Store the board as a string
        self.Computer = Comp(self)
        self.Human = Human(self)
        self.ComputerWin = False

    def startGame(self):
        if self.starter == 1:
            print("Computer starts")
            return self.CompStarts()
        else:
            print("Human starts")
            return self.HumanStarts()

    def CompStarts(self):
        while not self.isGameOver():
            print("Computer Turn")
            self.Computer.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            self.printableBoard(self.board)  # Convert the board to a list for printing
            if self.isGameOver():
                break
            print("Human Turn")
            self.Human.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            self.printableBoard(self.board)  # Convert the board to a list for printing
        if self.isWinner('X'):
            self.ComputerWin = True
        return self.boards, self.ComputerWin

    def HumanStarts(self):
        while not self.isGameOver():
            print("Human Turn")
            self.Human.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            self.printableBoard(self.board)  # Convert the board to a list for printing
            if self.isGameOver():
                break
            print("Computer Turn")
            self.Computer.getTurn()
            self.boards.append(self.convertToNormalStringForBoards(self.board))
            self.printableBoard(self.board)  # Convert the board to a list for printing
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
            # Use a custom decoding function to preserve the tuple data type
            return json.load(json_file, object_hook=lambda item: {k: tuple(v) for k, v in item.items()})

    def save_dict_to_json(self, Dict):
        with open('Dict.json', 'w') as json_file:
            # Use a custom encoding function to convert tuples to lists for JSON
            json.dump(Dict, json_file, default=lambda item: {k: list(v) for k, v in item.items()})

    def __init__(self):
        self.game = Game()
        self.Dict = self.load_dict_from_json()

    def startGame(self):
        self.Dict = self.load_dict_from_json()
        boards, compWon = self.game.startGame()
        print(boards)
        print(compWon)
        boards.reverse()
        self.DictionaryUpdating(boards, compWon)
        # print(self.Dict)
        self.save_dict_to_json(self.Dict)
        return compWon

    def getBoard(self):
        return self.game.getBoard()

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


class TicTacToeApp(App):

    def build(self):
        self.games = Games()
        self.game = self.games.game
        self.grid = GridLayout(cols=3)
        self.buttons = [Button(text=str(i), font_size='48sp') for i in range(1, 10)]
        self.playerShape = str(self.game.getStarter())
        self.computerShape = ''
        if int(self.playerShape) == 0:
            self.playerShape = 'X'
            self.computerShape = 'O'
        else:
            self.playerShape = 'O'
            self.computerShape = 'X'

        if self.game.getStarter() == 1:
            self.computerTurn()
        for i, button in enumerate(self.buttons):
            button.bind(on_release=lambda btn, idx=i: self.player_turn(idx))
            self.grid.add_widget(button)

        return self.grid

    def computerTurn(self):
        if not self.game.isGameOver():
            self.games.game.Computer.getTurn()
            self.updateBoard()
            if self.games.game.isGameOver():
                self.end_game("Computer wins!" if self.games.game.isWinner(self.computerShape) else "It's a draw!")

    def updateBoard(self):
        board = self.games.game.getBoard()
        for i, cell in enumerate(board):
            self.buttons[i].text = cell

    def player_turn(self, place):
        board = self.games.getBoard()
        if board[place] not in 'XO':
            self.games.game.Human.board = board[:place] + str(self.playerShape) + board[place + 1:]
            self.games.game.setBoard(self.games.game.Human.board)
            self.updateBoard()
            if self.games.game.isGameOver():
                self.end_game("You win!" if self.games.game.isWinner(self.playerShape) else "It's a draw!")
            else:
                self.computerTurn()

    def end_game(self, message):
        popup = Popup(title='Game Over',
                      content=Label(text=message),
                      size_hint=(None, None), size=(200, 200))
        popup.open()


if __name__ == '__main__':
    TicTacToeApp().run()
