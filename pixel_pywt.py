import numpy as np
import pywt
from Functions.split_matrices import split_matrices
from matplotlib import pyplot as plt
from Functions.mtrxHaar import mtrxHaar

N = 128
K = 2
m = 3
n = 5
lvl = 2

vect = 'WV'
f = np.zeros((N,N))

if vect == 'VW':
    f[int(3/4*N)-n,(m-1)] = 1
elif vect == 'VV':
    f[N-n,(m-1)] = 1
elif vect == 'WW':
    f[int(3/4*N)-n,int(N/4)+(m-1)] = 1
elif vect == 'WV':
    f[N-n,int(N/4)+(m-1)] = 1
else:
    print('Error: tensor_type is not correct')

fig,ax = plt.subplots(1,1)
plt.imshow(f, cmap='gray_r', interpolation='none')
plt.show()

# Inverse transform.
wavelet = 'haar'
inv_tr = np.empty(K, dtype='object')

cA, (cH, cV, cD) = split_matrices(f[N//2:,:N//2])
inv_tr[1] = f.copy()
inv_tr[1][N//2:,:N//2] = pywt.idwt2((cA, (-cH, cV, -cD)), wavelet)

cA, (cH, cV, cD) = split_matrices(inv_tr[1])
inv_tr[0] = pywt.idwt2((cA, (-cH, cV, -cD)), wavelet)

# Plot.
fig, axs = plt.subplots(ncols=K, nrows=1)
for k, ax in enumerate(axs.flat):
    ax.imshow(inv_tr[k], cmap='gray', interpolation='none')
    ax.set_title('Level ' + str(k))
    print(inv_tr[k])
plt.show()