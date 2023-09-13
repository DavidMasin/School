import numpy as np
import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


def is_magic_square(matrix):
    # Check the sums of rows, columns, and diagonals
    target_sum = np.sum(matrix[0])

    # Check diagonals
    if all(np.sum(matrix, 0) == target_sum) and all(np.sum(matrix, 1) == target_sum):
        if np.sum(np.diag(matrix)) != target_sum or np.sum(np.diag(np.fliplr(matrix))) != target_sum:
            return False

        return True

    # Check rows and columns
    return False


class MagicSquare:
    def __init__(self, n):
        self.n = n

    def generate_magic_square(self):
        # Generate a random 3x3 matrix with unique values from 1 to 9
        matrix = np.random.permutation(np.arange(1, 10)).reshape(3, 3)
        string_matrix = ''.join([str(elements) for row in matrix for elements in row])
        return string_matrix, is_magic_square(matrix)


def MakeDictionary(num):
    magic_square = MagicSquare(3).generate_magic_square()
    # print(magic_square)
    if magic_square in my_dict:
        print("This magic square is already in the dictionary")
        print(my_dict(magic_square))
    else:
        my_dict[num] = magic_square

    # print(my_dict)
    for key, value in my_dict.items():
        if value[1]:
            print(value[0])
    return my_dict
    '''
    my_dict = {}
    for i in range(500000):
        magic_square = MagicSquare(3).generate_magic_square()
        my_dict[i] = magic_square
    return my_dict
    '''


def PutInJson(my_dict):
    with open('Dic.json', 'w') as json_file:
        json.dump(my_dict, json_file)


class MyApp(App):
    def build(self):
        self.good_dic = {}  # Make good_dic an instance variable

        # Create the main GridLayout with two rows
        main_layout = GridLayout(rows=2)

        # Create a GridLayout for the labels in the top row
        label_layout = GridLayout(cols=3)
        counter = 0
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


if __name__ == '__main__':
    global my_dict
    with open('Dic.json', 'r') as json_file:
        my_dict = json.load(json_file)
    PutInJson(MakeDictionary(len(my_dict)))
    MyApp().run()