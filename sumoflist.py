list=[1,2,3,4,5,6]
i=0
sum=0
avg=0
while i<=len(list):
    sum=sum+i
    i+=1
print(sum)
avg=sum/len(list)
print(avg)

# list=[1,2,3,4,5,6]       # sum using for loop
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)
# avg=sum/i
# print(avg)