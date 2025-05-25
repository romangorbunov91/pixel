import numpy as np
def vwHaar(N):
    if ((N > 1)&((N % 2) == 0)):
        N_alpha = 2
        alpha = np.zeros((1,N_alpha))
        alpha[0,0] = 1 / np.sqrt(2)
        alpha[0,1] = 1 / np.sqrt(2)
        
        N_beta = N_alpha
        beta = np.zeros((1,N_beta))
        beta[0,0] = 1 / np.sqrt(2)
        beta[0,1] = -1 / np.sqrt(2)
        
        V = np.zeros((int(N/2),N))
        W = np.zeros((int(N/2),N))
        
        for idx in range(int(N/2)):
            V[idx,(2*idx):(2*idx+N_alpha)] = alpha
            W[idx,(2*idx):(2*idx+N_beta )] = beta
    else:
        print('USER ERROR: Length (N) is incorrect!!!')
    return V, W