import numpy as np
import matplotlib.pyplot as plt
xp = np.random.randint(100,size =(100))
yp = np.random.randint(100,size= (100))
colors = np.random.randint(100,size = (100))
sizes = 10*np.random.randint(100,size = (100))

plt.scatter(xp,yp,c =colors,s =sizes,cmap = 'nipy_spectral',alpha = 0.5)
plt.colorbar()
plt.show()