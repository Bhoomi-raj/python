import numpy as np
import matplotlib.pyplot as plt
##plot 1
xp = np.array([10,20,30,40])
yp = np.array([1,9,3,4])
plt.subplot(2,3,1)
plt.title("time")
#--------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
colors = np.array(["red","pink","blue","grey"])
#plt.plot(xp,yp)
plt.scatter(xp,yp,c=colors)


##plot 2
xp = np.array([1,9,4,6,5])
yp = np.array([10,19,23,14,2])
plt.subplot(2,3,2)
plt.title("sale")
#plt.plot(xp)
plt.scatter(xp,yp,color = 'black')
##plot 3
xp = np.array([1,2,8,7,6])
yp = np.array([10,19,23,24,23])
plt.subplot(2,3,3)
plt.title("diff")
#plt.plot(xp)
plt.scatter(xp,yp,color = 'hotpink')
#plot 4
xp = np.array([10,19,14,16,25])
yp = np.array([11,19,23,34,13])
plt.subplot(2,3,4)
plt.title("laugh")
#plt.plot(xp)
plt.scatter(xp,yp,color = 'grey')
#plot 5
xp = np.array([11,21,31,61,51])
yp = np.array([1,19,43,44,13])
plt.subplot(2,3,5)
plt.title("race")
#plt.plot(xp)
plt.scatter(xp,yp)
#plot 6
xp = np.array([5,6,7,8,9])
yp = np.array([12,92,32,42,20])
plt.subplot(2,3,6)
plt.title("dist")
# plt.plot(xp)
plt.scatter(xp,yp)

plt.suptitle("my room")
plt.show()