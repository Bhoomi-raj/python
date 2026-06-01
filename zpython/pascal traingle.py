# x = int(input("enter number of rows "))
# pascal =[]
# for i in range(x):
#     row = [1]*(i+1)
#     for j in range(1,i):
#         row[j] = pascal[i-1][j] + pascal[i-1][j-1]
            
#     pascal.append(row)       
# print(pascal,end = "")    

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def nCr(i,j):
    nemo = fact(i)
    demo = fact(j)*fact(i-j)
    return nemo//demo
x = int(input("enter number of rows "))
pascal = []
for i in range(x):
    row = [1]*(i+1)
    for j in range(1,i):
       row[j] = nCr(i,j)
       pascal.append(row)
print(pascal)         


