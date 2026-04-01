# import matplotlib
# print(matplotlib.__version__)
#--------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# xpt = np.array([1,2])
# ypt = np.array([3,4])
# plt.plot(xpt,ypt,marker ='o')
# plt.show()
#--------------------------------------------------------
# x_axis1 = np.array([2,4,7,9])
# x_axis2 = np.array([5,7,6,1,0])
#plt.plot(x_axis,'o:b')
#plt.show()
#plt.plot(y_axis,marker = '*',ms = 13,mec = 'g')
#plt.show()################ for face colour use mfc
#### for line style use ls or line style
# plt.plot(y_axis,linestyle = 'dashed',color = 'b',linewidth = 15.6)
# plt.show()
### or use ls for line style or c for color
# plt.plot(x_axis1)
# plt.plot(x_axis2)
#plt.show()
#-------------------------------------------------------------------------
xp = np.array([10,20,30,40,50,60,70,80,90])
yp = np.array([1,2,3,4,5,6,7,8,9])
plt.plot(xp,yp)
plt.xlabel("velocity")
plt.ylabel("time")
plt.show()