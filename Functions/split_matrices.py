def split_matrices(matrix):
    Nrow, Mcol = matrix.shape
    if Nrow % 2 != 0 or Mcol % 2 != 0:
        raise ValueError("Число строк и столбцов должно быть четным!")
    
    half_rows = Nrow // 2
    half_cols = Mcol // 2
    
    # Book's way.
    cA = matrix[half_rows:, :half_cols]
    cH = matrix[:half_rows, :half_cols]
    cV = matrix[half_rows:, half_cols:]
    cD = matrix[:half_rows, half_cols:]
    
    '''
    # PyWavelet way.
    cA = matrix[:half_rows, :half_cols]
    cH = matrix[:half_rows, half_cols:]
    cV = matrix[half_rows:, :half_cols]
    cD = matrix[half_rows:, half_cols:]
    '''

    return cA, (cH, cV, cD)