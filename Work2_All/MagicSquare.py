import json

import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


def is_magic_square(matrix):  # בודק האם הריבוע שניתן הוא ריבוע הקסם
    target_sum = np.sum(matrix[0])  # לוקח סכום אחד של שורה (כי כולם צריכים להיות שווים)

    if all(np.sum(matrix, 0) == target_sum) and all(np.sum(matrix, 1) == target_sum):  # בודק האם כל האפשרויות של הסכום שוות אחת לשנייה
        if np.sum(np.diag(matrix)) != target_sum or np.sum(np.diag(np.fliplr(matrix))) != target_sum:#בודק האם האלכסונים שווים
            return False

        return True
    #אם הסכומים לא שווים אחד לשני אז זה לא ריבוע הקסם
    return False


class MagicSquare:  # יוצר ריבוע קסם חדש
    def __init__(self, n):  # בנאי שמקבל את אורך העמודות והשורות (אותו מספר)
        self.n = n

    def generate_square(self):  # יוצר ריבוע
        matrix = np.random.permutation(np.arange(1, 10)).reshape(3, 3)  # יוצר מטריצה עם מספרים במקומות רנדומליים
        string_matrix = ''.join(
            [str(elements) for row in matrix for elements in row])  # יוצר משתנה חדש ששומר את המטריצה בתור String
        return string_matrix, is_magic_square(matrix)


def MakeDictionary():  # יוצר מילון
    #for i in range(100000):
    magic_square = MagicSquare(3).generate_square()  # מגריל ריבוע חדש
    # print(magic_square)
    if (magic_square[0]) in my_dict.items():  # בודק האם הריבוע כבר במילון
        print("This magic square is already in the dictionary")
    else:
        my_dict[magic_square[0]] = magic_square[1]  # אם לא מכניס אותו למילון
    # print(my_dict)
    for key, value in my_dict.items():
        if value:  #  זה האם הריבוע הוא ריבוע הקסם כן או לא
            print(key)  #  זה המחרוזת של ריבוע הקסם
    return my_dict

    # my_dict = {}
    # for i in range(500000):
    #     magic_square = MagicSquare(3).generate_square()
    #     my_dict[i] = magic_square
    # return my_dict


def PutInJson(my_dict):  # בשביל לעדכן את המילון
    with open('Dic.json', 'w') as json_file:
        json.dump(my_dict, json_file)


class MyApp(App):  # האפליקציה
    def build(self):  # הבנאי של האפליקציה
        self.good_dic = {}  # ריבועי הקסם הטובים יהיו פה

        # יוצר את הלייאוט הראשי
        main_layout = GridLayout(rows=2)

        label_layout = GridLayout(cols=3)
        counter = 0  # סופר את כמות המספרים של ריבועי הקסם הטובים
        for key, value in my_dict.items():
            if value:
                self.good_dic[counter] = key
                counter += 1

        # יוצר את הלייאוט של הלייבלים
        self.MakeLabels(label_layout)

        button_layout = GridLayout(cols=1)
        # יוצרים כפתור בשביל לשנות את ריבוע הקסם
        button = Button(text='Change Square')
        button.bind(on_press=self.change_text)
        button.width = 50
        button_layout.add_widget(button)

        # מוסיף את הלייאוטים למיין לייאוט
        main_layout.add_widget(label_layout)
        main_layout.add_widget(button_layout)

        # מתחיל מריבוע הקסם הראשון
        self.which_square = 0
        self.update_labels(self.which_square)
        return main_layout

    def MakeLabels(self, label_layout):  # יוצר את הלייאוט של הלייבלים
        self.labels = []
        for column in range(3):
            row_labels = []
            for row in range(3):
                img = Image(
                    source=r'C:\Users\user\PycharmProjects\School\Work2_All\placeholder.png')  # or use the actual name of your placeholder image
                label_layout.add_widget(img)
                row_labels.append(img)
            self.labels.append(row_labels)

    def change_text(self, instance):
        # מחליף את הריבוע הקסם
        self.which_square = (self.which_square + 1) % len(self.good_dic)  # עובר לריבוע הקסם הבא
        self.update_labels(self.which_square)  # מעדכן את הלייבלים

    def update_labels(self, square_index):  # מעדכן את הלייבלים
        for i in range(3):  # עובר על כל הלייבלים
            for j in range(3):
                label = self.labels[i][j]
                img_path = r'C:\Users\user\PycharmProjects\School\Work2_All\{}.png'.format(
                    self.good_dic[square_index][i * 3 + j])
                label.source = img_path
                label.reload()


def GettingDic():
    global my_dict
    with open('Dic.json', 'r') as json_file:
        my_dict = json.load(json_file)


if __name__ == '__main__':
    global my_dict
    GettingDic()
    PutInJson(MakeDictionary())
    MyApp().run()
