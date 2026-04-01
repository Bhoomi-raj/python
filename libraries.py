# # # import numpy as np
# # # arr =np.array([1,2,3,4,5])
# # # print(arr)
# # import numpy as np
# # arr = np.array([[1,2,3],[4,5,6],[5,6,7]])
# # print(arr.ndim)
# # brr = np.array([
# #     [[1,2,3],[4,5,6]],
# #     [[6,7,8],[10,11,45]]
# # ])
# # print(brr.ndim)
# import numpy as np
# arr = np.array([[1,2,3,4,5],[11,32,45,61,15]])
# brr =np.array([1,2,3,4,5],dtype='S')
# #------------------print(arr[1:5])
# # print(arr[1:6:2])
# # print(arr[::2])
# # print(arr[0,0:])
# # crr = np.array(["apple","chair","table"])
# # print(crr.dtype)
# print(brr.dtype)
#----------------------------------------------------------------------
# import numpy as np
# arr = np.array([1.1,2.2,3.3,4.3,5.5,6.5])
# brr = arr.astype('i')
# print(brr)
# print(brr.dtype)
#-----------------------------------------------------------------------
import numpy as np
# arr = np.array([1,2,3,4,5])
# a = arr.copy()
# a[0] = 43
# print(arr)
# print(a)
# brr = np.array([1,2,3,4,5])
# c = brr.view()
# c[0] = 24
# print(brr)
# print(c)
d = np.array([[1,2,3,4,5],[7,8,9,0,1]])
x = d[0:5]

print(x.flags.owndata)
print(d.flags.owndata)
d[0] =21
print(d)
print(x)
print(d.shape)
f = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(f.reshape(4,4).base)