# Ex. 4.1.C.
import numpy as np
from Functions.mtrxHaar import mtrxHaar
from matplotlib import pyplot as plt

def delta(x):
    if int(x) == 0:
        return int(1)
    else:
        return int(0)

Np = 128
K = 2

m = 3
n = 5
lvl = 2

V,W = mtrxHaar(Np,2)

V3 = np.matrix(V[lvl-1][m-1])
V5 = np.matrix(V[lvl-1][n-1])
W3 = np.matrix(W[lvl-1][m-1])
W5 = np.matrix(W[lvl-1][n-1])

V3W5 = np.transpose(np.flip(W5)) * V3
W3W5 = np.transpose(np.flip(W5)) * W3
V3V5 = np.transpose(np.flip(V5)) * V3
W3V5 = np.transpose(np.flip(V5)) * W3
WVplot = [V3W5, W3W5, V3V5, W3V5]

# Plot.
fig, axs = plt.subplots(ncols=2, nrows=2)
for idx, ax in enumerate(axs.flat):
    ax.imshow(WVplot[idx], cmap='gray', interpolation='none', vmin=-0.25, vmax=0.25)
plt.savefig('readme_img/tensors.png', bbox_inches='tight')
plt.show()