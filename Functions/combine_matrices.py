import numpy as np

# Book's way.
def combine_matrices(cA, cH, cV, cD):
    top_row = np.hstack((cH, cD))
    bottom_row = np.hstack((cA, cV))
    return np.vstack((top_row, bottom_row))