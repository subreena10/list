list=[8,7,6,1,2,4,3,4,5]
new_list=[]
i=0
while i<len(list):
    maximum=list[i]
    for x in list:
        if x>maximum:
            maximum=x
    new_list.append(maximum)
    list.remove(maximum)
print(new_list)

