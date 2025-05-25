# Ex. 4.1.C.

import numpy as np
from Functions.mtrxHaar import mtrxHaar
from Functions.vwHaar import vwHaar
from Functions.mtrxCoif6 import mtrxCoif6
from matplotlib import pyplot as plt

def delta(x):
    if int(x) == 0:
        return int(1)
    else:
        return int(0)

L = 64
Np = 128
K = 2

V, W = vwHaar(Np)

V3 = np.matrix(V[3-1])
V5 = np.matrix(V[5-1])
W3 = np.matrix(W[3-1])
W5 = np.matrix(W[5-1])

V3W5 = np.transpose(np.flip(W5)) * V3
W3W5 = np.transpose(np.flip(W5)) * W3
V3V5 = np.transpose(np.flip(V5)) * V3
W3V5 = np.transpose(np.flip(V5)) * W3
WVplot = [V3W5, W3W5, V3V5, W3V5]

# Plot.
fig, axs = plt.subplots(ncols=2, nrows=2)
for idx, ax in enumerate(axs.flat):
    ax.imshow(WVplot[idx], cmap='gray', interpolation='none', vmin=-0.5, vmax=0.5)
plt.show()
#=================================================================

'''
x = y = np.linspace(-L,L-1,Np)
f = np.zeros((Np,Np))
for n, y_val in enumerate(y):
    for m, x_val in enumerate(x):
        f[n,m] = delta((x_val + 64 - 2)) * delta(y_val + 32 - 4)
f = np.flipud(f)
fig,ax = plt.subplots(1,1)
plt.imshow(f, cmap='gray_r', interpolation='none', vmin=0, vmax=1)
plt.show()

f = np.matrix(f)
num_row = np.shape(f)[0]
num_col = np.shape(f)[1]


# Inverse transform.
rev_col_tr = np.empty(K, dtype='object')
sub_tr     = np.empty(K, dtype='object')
rev_tr     = np.empty(K, dtype='object')

for k in reversed(range(K)):
    [Mdir, Mrev] = mtrxHaar(int(Np/2**k),1)
    sub_tr[k] = np.matrix(np.zeros((int(Np/2**k),int(Np/2**k))))
    rev_col_tr[k] = np.flipud(Mrev[0]*np.flipud(f[int(Np-Np/2**k):Np,:int(Np/2**k)]))
    sub_tr[k] = rev_col_tr[k] * np.transpose(Mrev[0])
    rev_tr[k] = f.copy()
    rev_tr[k][int(Np-Np/2**k):Np,:int(Np/2**k)] = sub_tr[k]

# Plot.
fig, axs = plt.subplots(ncols=K, nrows=1)
for idx, ax in enumerate(axs.flat):
    ax.imshow(rev_tr[idx], cmap='gray', interpolation='none', vmin=-0.5, vmax=0.5)
    #ax.set_title('Level ' + str(idx))
plt.show()
#=================================================================
'''

'''
x = y = np.linspace(-L,L-1,Np)
f = np.zeros((Np,Np))
for n, y_val in enumerate(y):
    for m, x_val in enumerate(x):
        #f[n,m] = delta((x_val + 64 - 2)) * delta(y_val + 32 - 4)
        f[n,m] = delta((x_val - 62)) * delta(y_val - 28)
f = np.flipud(f)
fig,ax = plt.subplots(1,1)
plt.imshow(f, cmap='gray_r', interpolation='none', vmin=0, vmax=1)
plt.show()
[Mdir, Mrev] = mtrxHaar(Np,K)
rev_col_tr = np.flipud(Mrev[1]*f)
rev_tr = rev_col_tr * np.transpose(Mrev[1])    

plt.imshow(rev_tr, cmap='gray', interpolation='none', vmin=-0.5, vmax=0.5)
plt.show()
'''