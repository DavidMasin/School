import random

import kivy.uix.button
import numpy as np
import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MineSweeper:#המשחק
    def __init__(self, row, col, PercentageOfMines):#הבנאי של המשחק, מקבל את כמות השורות, העמודות ויחס הפצצות
        self.row = row + 2#מגדיל ב2 את השורות בשביל הלוח הלוגי
        self.col = col + 2#מגדיל ב2 את מספר העמודות בשביל הלוח הלוגי
        self.LogicMatrix = np.zeros((self.row, self.col))#יוצר numpy חדש מאופס שהגודל שלו הוא גודל הלוח הלוגי
        self.PercentageOfMines = PercentageOfMines
        self.mine_positions = []#מקום הפצצות

    def insert_mines(self):#הכנסת הפצצות למשחק
        center_rows = self.row - 2#מכניס פצצות רק בשורות שניתן לראות
        center_cols = self.col - 2#כנל עמודות
        total_center_elements = center_rows * center_cols#מוצא את מספר הכפתורים שעליהם ניתן ללחוץ
        elements_to_replace = int(total_center_elements * self.PercentageOfMines)#מוצא את כמות הכפתורים שיש להחליף לפצצות

        self.RandomPositionForMines(elements_to_replace)#זימון פעולה

        for x, y in self.mine_positions:#מחליף את המקומות שהוגרלו בתור מקום לפצצה במספר 11
            self.LogicMatrix[x][y] = 11

    def RandomPositionForMines(self, elements_to_replace):#מוצא מקום רנדומלי לפצצות ומכניס את זה למערך הפצצות
        positions = [(x, y) for x in range(1, self.row - 1) for y in range(1, self.col - 1)]#מוצא את כל האופציות האפשרויות
        self.mine_positions = random.sample(positions, elements_to_replace)#בוחר מהאופציות את הכמות הרצויה בצורה רנדומלית ומכניס את זה למערך "מקום הפצצות"



    def StartGame(self):#מתחיל משחק
        #print("Original Matrix")
        #print(self.LogicMatrix)
        self.insert_mines()
        #print("Matrix with mines")
        #print(self.LogicMatrix)
        #print("Matrix with mines and numbers")
        #print(self.LogicMatrix)
        #print(self.mine_positions)

    #Getter and Setter
    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getLogicMatrix(self):
        return self.LogicMatrix

    def getMinePositions(self):
        return self.mine_positions


class MyApp(App):

    def __init__(self):#הגדרת מאתחל בשביל משתנים שאני משתמש בכמה פעולות שונות Buttons ישמור את כל המקומות של הכפתורים וGAME ישמור את המשחק עצמו
        super().__init__()
        self.buttons = {}  # Store the buttons with their coordinates as keys
        self.game = None

    def build(self):#בונה משחק מוקשים חדש
        row = 20#כמות השורות של המשחק עצמו
        col = 15#כמות העמודות במשחק עצמו
        percentage_of_mines = 1 / 6#יחס המוקשים
        self.game = MineSweeper(row, col, percentage_of_mines)#הגדרת המשחק, אומרים את כמות השורות, כמות העמודות ואת יחס המוקשים
        self.game.StartGame()#מתחילים משחק
        main_layout = GridLayout(rows=row, cols=col)#יוצרים GRIDLAYOUT חדש בשביל הKivi

        for i in range(1, row + 1):#שם בתוך האפליקציה כפתורים בגודל של המשחק שרשום אליהם Hidden
            for j in range(1, col + 1):
                btn = Button(text="hidden")
                btn.bind(on_press=self.on_button_press)
                main_layout.add_widget(btn)
                self.buttons[(i, j)] = btn

        return main_layout

    def on_button_press(self, instance):#
        coords = [key for key, btn in self.buttons.items() if btn == instance][0]#הקורדינתות של הכפתור
        #print(coords)
        value = self.game.getLogicMatrix()[coords[0], coords[1]]#הערך של הכפתור שנלחץ
        #print(value)

        if instance.text == "hidden":#הוא בודק האם הכפתור כבר נלחץ אם הוא כבר נלחץ לא יהיה ניתן ללחוץ עליו עוד הפעם
            if value == 11:  # נלחצה פצצה
                self.end_game()#מחליף את הכפתורים לYOU LOST
                self.reveal_all_bombs()#משנה את השם של הכפתורים שהם פצצות (11) לX

            else:
                if value == 0:#אם נלחץ אפס הוא יתחיל לפתוח מסביבו את המספרים בצורה רקורסיבית
                    self.reveal_adjacent_zeros(coords[0], coords[1])
                else:
                    instance.text = str(int(value))#אם נלחץ מספר הוא פשוט מראה את המספר

    def reveal_all_bombs(self):
        for (x, y) in self.game.getMinePositions():#הוא עובר על כל הקורדינתות של הפצצות ומחליף את שם הכפתור לX
            self.buttons[(x, y)].text = "X"

    def reveal_adjacent_zeros(self, row, col, visited=None):#אם נלחץ אפס צריך להתרחב עד שנמצא מספר, מתרחבים לכל כיוון
        if visited is None:#בודק האם זאת הפעם הראשונה
            visited = set()#אם כן, מגדיר אובייקט חדש שבו יזכור את כל המקומות שבהם היה

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]#כל הoffset שצריך לעשות מהכפתור שהוא 0
        for dx, dy in directions:#הולך לכל כיוון
            x, y = row + dx, col + dy
            if 1 <= x < self.game.getRow() - 1 and 1 <= y < self.game.getCol() - 1 and (x, y) not in visited:  # מוודא שהוא כבר לא עבר על הכפתור וגם הוא נמצא בתוך גבולות המשחק
                visited.add((x, y))#מכניס את הקורדינתות לVisited בשביל שלא יעבור על הכפתור שנית
                # print("Visited: ", visited)
                val = self.game.getLogicMatrix()[x, y]#ערך הכפתור
                if val == 0:#אם הכפתור 0 ממשיכים להתרחב בצורה רקורסיבית
                    self.buttons[(x, y)].text = "0"
                    self.reveal_adjacent_zeros(x, y, visited)#רקורסיה
                elif val != 11: #מוודא שהוא לא מראה פצצה, אבל מראה מספר
                    self.buttons[(x, y)].text = str(int(val))

    def end_game(self):#משנה את כל הכפתורים ל"YOU LOST"
        for btn in self.buttons.values():
            btn.text = "YOU LOST"

    def end_game_win(self):# כמו end_game רק YOU WON
        for btn in self.buttons.values():
            btn.text = "YOU WON!"


if __name__ == '__main__':
    MyApp().run()
