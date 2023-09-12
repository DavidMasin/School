import numpy as np


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


def generate_magic_square():
    numbers=0
    while True:
        numbers+=1
        # Generate a random 3x3 matrix with unique values from 1 to 9
        matrix = np.random.permutation(np.arange(1, 10)).reshape(3, 3)

        if is_magic_square(matrix):
            return matrix,numbers

def main():
    magic_square = generate_magic_square()
    print("Random 3x3 Magic Square:")
    print(magic_square)


main()
