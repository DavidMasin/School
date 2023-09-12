import random

import kivy.uix.button
import numpy as np
import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MineSweeper:
    def __init__(self, row, col, PercentageOfMines):
        self.row = row + 2
        self.col = col + 2
        self.LogicMatrix = np.zeros((self.row, self.col))
        self.PercentageOfMines = PercentageOfMines
        self.mine_positions = []

    def insert_mines(self):
        center_rows = self.row - 2
        center_cols = self.col - 2
        total_center_elements = center_rows * center_cols
        elements_to_replace = int(total_center_elements * self.PercentageOfMines)

        self.RandomPositionForMines(elements_to_replace)

        # Replace the selected positions with 11s
        for x, y in self.mine_positions:
            self.LogicMatrix[x][y] = 11

    def RandomPositionForMines(self, elements_to_replace):
        positions = [(x, y) for x in range(1, self.row - 1) for y in range(1, self.col - 1)]
        self.mine_positions = random.sample(positions, elements_to_replace)

    def count_mines(self):
        for x, y in self.mine_positions:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if self.LogicMatrix[i][j] != 11:
                        self.LogicMatrix[i][j] += 1

    def StartGame(self):
        print("Original Matrix")
        print(self.LogicMatrix)
        self.insert_mines()
        print("Matrix with mines")
        print(self.LogicMatrix)
        self.count_mines()
        print("Matrix with mines and numbers")
        print(self.LogicMatrix)
        print(self.mine_positions)

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getLogicMatrix(self):
        return self.LogicMatrix

    def getMinePositions(self):
        return self.mine_positions


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__()
        self.on_game_over = None
        self.buttons = {}  # Store the buttons with their coordinates as keys
        self.game = None

    def build(self):
        row = 20
        col = 15
        percentage_of_mines = 1 / 6
        self.game = MineSweeper(row, col, percentage_of_mines)
        self.game.StartGame()
        main_layout = GridLayout(rows=row, cols=col)

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                btn = Button(text="hidden")
                btn.bind(on_press=self.on_button_press)
                main_layout.add_widget(btn)
                self.buttons[(i, j)] = btn

        return main_layout

    def on_button_press(self, instance):
        coords = [key for key, btn in self.buttons.items() if btn == instance][0]
        value = self.game.getLogicMatrix()[coords[0], coords[1]]

        # If the button has not been opened or flagged, process it
        if instance.text == "hidden":
            if value == 11:  # bomb
                self.end_game()
                self.reveal_all_bombs()

            else:
                if value == 0:
                    self.reveal_adjacent_zeros(coords[0], coords[1])
                else:
                    instance.text = str(int(value))

    def reveal_all_bombs(self):
        for (x, y) in self.game.getMinePositions():
            self.buttons[(x, y)].text = "X"  # Representing bomb with 'X'

    def reveal_adjacent_zeros(self, row, col, visited=None):
        if visited is None:
            visited = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 1 <= r < self.game.getRow() - 1 and 1 <= c < self.game.getCol() - 1 and (
                    r, c) not in visited:  # Ensure you stay within inner grid bounds
                visited.add((r, c))
                val = self.game.getLogicMatrix()[r, c]
                if val == 0:
                    self.buttons[(r, c)].text = "0"
                    self.reveal_adjacent_zeros(r, c, visited)
                elif val != 11:  # Don't reveal the mines
                    self.buttons[(r, c)].text = str(int(val))

    def end_game(self):
        for btn in self.buttons.values():
            btn.text = "YOU LOST"

    def end_game_win(self):
        for btn in self.buttons.values():
            btn.text = "YOU WON!"


if __name__ == '__main__':
    MyApp().run()
