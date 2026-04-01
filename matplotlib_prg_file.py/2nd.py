import numpy as np
import matplotlib.pyplot as plt
x_axis = np.array([1,2,3,4,5,6])
y_axis = np .array([10,20,30,40,50,60])
#giving font style to x albel and y label 
font1 = {'family' : 'serif' , 'color' : 'darkred' , 'size' : 15}
font2 = {'family' : 'monospace' , 'color' : 'darkgrey' , 'size' : 20.5}



plt.plot(x_axis,y_axis)
#for giving x-axis label
plt.xlabel("time",fontdict=font1)
#for giving y-axis label
plt.ylabel("velocity",fontdict= font1)
#for giving title to grap
#we can use loc for location of titlte default centre 
plt.title("time v/s velocity",fontdict=font2,loc = 'left')
#to add or show grid 
#we can use plt.grid(axis = 'x') or axis ='y'
plt.grid(color = 'black',linestyle = '--' , linewidth = '0.5')
plt.show()