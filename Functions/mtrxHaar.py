import numpy as np
from Functions.vwHaar import vwHaar
def mtrxHaar(N,K):
    if ((N > 1)&((N % 2) == 0)):
        
        Mtrx = np.empty((K,), dtype=object)
        Mdir = np.empty((K,), dtype=object)
        Mrev = np.empty((K,), dtype=object)
        
        for k in range(K):
            
            Mtrx[k] = np.matrix(np.concatenate(vwHaar(int(N/2**k)), axis = 0))
            if k == 0:
                Mdir[0] = Mtrx[0].copy()
            else:
                Mdir[k] = np.identity(N)
                Mdir[k][:(int(N/2**k)),:(int(N/2**k))] = Mtrx[k][:(int(N/2**k)),:(int(N/2**k))].copy()
                #Mdir[k][int(N-N/2**k):N,int(N-N/2**k):N] = Mtrx[k][:int(N/2**k),:int(N/2**k)].copy()
                Mdir[k] = Mdir[k] * Mdir[k-1]
            Mrev[k] = np.linalg.inv(Mdir[k][:,:])
        
        return Mdir, Mrev
    else:
        print('USER ERROR: Length (N) is incorrect!!!')