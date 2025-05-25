import numpy as np

# Book approach.
def combine_matrices(cA, cH, cV, cD):
    top_row = np.hstack((cH, cD))
    bottom_row = np.hstack((cA, cV))
    return np.vstack((top_row, bottom_row))
'''
# PyWavelet approah.
def combine_matrices(cA, cH, cV, cD):
    top_row = np.hstack((cA, cH))
    bottom_row = np.hstack((cV, cD))
    return np.vstack((top_row, bottom_row))
'''