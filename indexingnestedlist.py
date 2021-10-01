a=[1,2,3,4,[5,6,7]]               #to find indecing of nested list  
i=0
while i<len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            print(i,j,a[i][j])
            j=j+1
    else:
        print(i,a[i])
    i=i+1