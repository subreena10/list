list=['a','d','j','e','i','k']
new_list=[]
i=0
while i<len(list):
    mininum=list[i]
    for x in list:
        if x<mininum:
            mininum=x
    new_list.append(mininum)
    list.remove(mininum)
print(new_list)


# i=0
# # a=[]
# min=list[i]
# while i<len(list):
#     if i<min:
#         min=list[i]
#         # a.append(min)
#         # list.remove(min)
#     i=i+1
# # print(a)
# print(min)


