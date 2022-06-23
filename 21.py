import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt


def DiagDom(A) -> None:
    """Function that checks if the given matrix is diagonal dominant or not."""
    diag_coeff = np.diag(np.abs(A))
    row_sum = np.sum(np.abs(A), axis=1) - diag_coeff
    if np.all(diag_coeff > row_sum):
        print("\nMatrix is Diagonally Dominant")
    else:
        print("\nNOT Diagonally Dominant")
    return

def generate_Diag_Dominant_matrix():
    """
    This function will generate diagonal dominant martix.
    This function may take time as matrix generation is completely random.
    """
    flag = True
    iteration_counter = 0
    while flag:
        A = np.random.randint(-10, 10, size=(4, 4))
        diag_coeff = np.diag(np.abs(A))
        row_sum = np.sum(np.abs(A), axis=1) - diag_coeff
        if np.all(diag_coeff > row_sum):
            flag = False
        else:
            flag = True
        iteration_counter += 1
    # print(f"Diagonal dominant martix Iteration completed after {iteration_counter} iterations")
    print(A)
    return A

