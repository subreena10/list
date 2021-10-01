number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
new_list=[]
while i<len(n):
    j=0
    while i>j:
        if n[i]+n[j]==number:
            new_list.append([n[i],n[j]])
        j=j+1
    i=i+1
print(new_list)


