a=[1,2,3,4,[5,6,7]]
n=len(a)
for i in range(n):
    if type(a[i]) is list:  
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])