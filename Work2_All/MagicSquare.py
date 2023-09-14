import numpy as np
import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


def is_magic_square(matrix):#בודק האם הריבוע שניתן הוא ריבוע הקסם
    # Check the sums of rows, columns, and diagonals
    target_sum = np.sum(matrix[0])#לוקח סכום אחד של שורה (כי כולם צריכים להיות שווים)

    if all(np.sum(matrix, 0) == target_sum) and all(np.sum(matrix, 1) == target_sum):#בודק האם כל האפשרויות של הסכום שוות אחת לשנייה
        if np.sum(np.diag(matrix)) != target_sum or np.sum(np.diag(np.fliplr(matrix))) != target_sum:
            return False

        return True

    # Check rows and columns
    return False


class MagicSquare:#יוצר ריבוע קסם חדש
    def __init__(self, n):#בנאי שמקבל את אורך העמודות והשורות (אותו מספר)
        self.n = n

    def generate_square(self):#יוצר ריבוע
        matrix = np.random.permutation(np.arange(1, 10)).reshape(3, 3)#  יוצר מטריצה עם מספרים במקומות רנדומליים
        string_matrix = ''.join([str(elements) for row in matrix for elements in row])#יוצר משתנה חדש ששומר את המטריצה בתור String
        return string_matrix, is_magic_square(matrix)


def MakeDictionary(num):#יוצר מילון
    magic_square = MagicSquare(3).generate_square()#מגריל ריבוע חדש
    # print(magic_square)
    if magic_square in my_dict:#בודק האם הריבוע כבר במילון
        print("This magic square is already in the dictionary")
        print(my_dict(magic_square))
    else:
        my_dict[num] = magic_square#אם לא מכניס אותו למילון

    # print(my_dict)
    for key, value in my_dict.items():
        if value[1]:#value[1] זה האם הריבוע הוא ריבוע הקסם כן או לא
            print(value[0])#value[0] זה המחרוזת של ריבוע הקסם
    return my_dict

    # my_dict = {}
    # for i in range(500000):
    #     magic_square = MagicSquare(3).generate_square()
    #     my_dict[i] = magic_square
    # return my_dict



def PutInJson(my_dict):#בשביל לעדכן את המילון
    with open('Dic.json', 'w') as json_file:
        json.dump(my_dict, json_file)


class MyApp(App):#האפליקציה
    def build(self):#הבנאי של האפליקציה
        self.good_dic = {}  # ריבועי הקסם הטובים יהיו פה

        # Create the main GridLayout with two rows
        main_layout = GridLayout(rows=2)

        # Create a GridLayout for the labels in the top row
        label_layout = GridLayout(cols=3)
        counter = 0#סופר את
        for key, value in my_dict.items():
            if value[1]:
                self.good_dic[counter] = value[0]
                counter += 1

        # Create a 3x3 grid of Label widgets and store them in a list
        self.labels = []
        for _ in range(3):
            row_labels = []
            for _ in range(3):
                label = Label()
                label_layout.add_widget(label)
                row_labels.append(label)
            self.labels.append(row_labels)

        # Create a GridLayout for the button in the bottom row
        button_layout = GridLayout(cols=1)
        # Create a button to change the text
        button = Button(text="Change Text")
        button.bind(on_press=self.change_text)
        button.size_hint = (None, None)
        button.width = 150  # Adjust the button width as needed
        button_layout.add_widget(button)

        # Add the label layout and button layout to the main layout
        main_layout.add_widget(label_layout)
        main_layout.add_widget(button_layout)

        # Initialize which_square
        self.which_square = 0
        self.update_labels(0)

        return main_layout

    def change_text(self, instance):
        # Update the labels
        self.which_square = (self.which_square + 1) % len(self.good_dic)
        self.update_labels(self.which_square)

    def update_labels(self, square_index):
        # Update the text of each label
        for i in range(3):
            for j in range(3):
                label = self.labels[i][j]
                label.text = self.good_dic[square_index][i * 3 + j]


def GettingDic():
    global my_dict
    with open('Dic.json', 'r') as json_file:
        my_dict = json.load(json_file)


if __name__ == '__main__':
    global my_dict
    GettingDic()
    PutInJson(MakeDictionary(len(my_dict)))
    MyApp().run()
