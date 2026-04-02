import numpy as np
import matplotlib.pyplot as plt
xp = np.array([1,2,3,4,5])
yp = np.array([10,20,30,40,50])
## for diff size of diff point
size = np.array([300,100,450,520,220])

## for diff color of diff point
#colors = np.array([10,15,20,25,30])
##cmap for colour map viridis or OrRd
plt.bar(xp,yp)
plt.xlabel("stress")
plt.ylabel("year")
#### to show colorbar in side of graph use
# plt.colorbar()
plt.title(" student")
plt.show()
