a=[1,2,3,4,[5,6,7]]
b=[]
i=0
sum=0
while i <len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            sum=sum+a[i][j]
            j+=1
    else:
        b.append(a[i])
        sum+=a[i]
    i+=1
print(b)
print(sum)


    







    