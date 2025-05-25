import numpy as np
from Functions.vwCoif6 import vwCoif6
def mtrxCoif6(N,K):
    if ((N > 1)&((N % 2) == 0)):
        
        Mtrx = np.empty((K,), dtype=object)
        Mdir = np.empty((K,), dtype=object)
        Mrev = np.empty((K,), dtype=object)
        
        for k in range(K):
            
            Mtrx[k] = np.matrix(np.concatenate(vwCoif6(int(N/2**k)), axis = 0))
            if k == 0:
                Mdir[0] = Mtrx[0]
            else:
                Mdir[k] = np.identity(N)
                Mdir[k][0:(int(N/2**k)-1),0:(int(N/2**k)-1)] = Mtrx[k][0:(int(N/2**k)-1),0:(int(N/2**k)-1)]
                Mdir[k] = Mdir[k] * Mdir[k-1]
            Mrev[k] = np.linalg.inv(Mdir[k][:,:])
        
        return Mdir, Mrev
    else:
        print('USER ERROR: Length (N) is incorrect!!!')