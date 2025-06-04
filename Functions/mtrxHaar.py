import numpy as np
from Functions.vwHaar import vwHaar
def mtrxHaar(N,K):
    if ((N > 1)&((N % 2) == 0)):
        
        Mtrx = np.empty((K,), dtype=object)
        Mdir = np.empty((K,), dtype=object)      
        V = np.empty((K,), dtype=object)
        W = np.empty((K,), dtype=object)
        for k in range(K):
            Mtrx[k] = np.matrix(np.concatenate(vwHaar(N//2**k), axis = 0))
            if k == 0:
                Mdir[0] = Mtrx[0].copy()
            else:
                Mdir[k] = np.identity(N)
                Mdir[k][:(N//2**k),:(N//2**k)] = Mtrx[k][:(N//2**k),:(N//2**k)].copy()
                Mdir[k] = Mdir[k] * Mdir[k-1]  
            V[k] = Mdir[k][:(N//2**(k+1)),:]
            W[k] = Mdir[k][(N//2**(k+1)):(N//2**k),:]
        return V,W
    else:
        print('USER ERROR: Length (N) is incorrect!!!')