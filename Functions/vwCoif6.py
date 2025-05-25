import numpy as np
def vwCoif6(N):
    if ((N > 1)&((N % 2) == 0)):
        N_alpha = 6
        alpha = np.zeros((1,N_alpha))
        alpha[0,0] = 1 - np.sqrt(7)
        alpha[0,1] = 5 + np.sqrt(7)
        alpha[0,2] = 14 + 2 * np.sqrt(7)
        alpha[0,3] = 14 - 2 * np.sqrt(7)
        alpha[0,4] = 1 - np.sqrt(7)
        alpha[0,5] = -3 + np.sqrt(7)
        
        alpha = alpha / (16 * np.sqrt(2))

        N_beta = N_alpha
        beta = np.zeros((1,N_beta))
        for idx in range(N_beta):
            beta[0,idx] =  (-1)**idx * alpha[0,(N_beta - 1) - idx]
        
        V = np.zeros((int(N/2),N))
        W = np.zeros((int(N/2),N))
        
        for idx in range(int(N/2)):
            indexVar = (N - 2 + 2*idx) % N
            for k in range(N_alpha):
                V[idx,indexVar] = alpha[0,k]
                W[idx,indexVar] = beta[0,k]
                indexVar = (indexVar + 1) % N
    else:
        print('USER ERROR: Length (N) is incorrect!!!')
    return V,W