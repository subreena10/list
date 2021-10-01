elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
total_sum=0
even_count=0
odd_count=0
total_count=0
avg=0
average=0
total_avg=0
while i<len(elements):
    if (elements[i]%2)==0:
        sum1=sum1+i
        even_count=even_count+1
    else:
        odd_count=odd_count+1
        sum=sum+i
    i+=1
total_sum=sum+sum1
print(total_sum,"total sum")
print(sum,"odd sum")
avg=sum/even_count
print(avg,"average of even")

print(sum1,"even sum")
average=sum1/odd_count
print(average,"avg of odd")

total_avg=total_sum/i
print(total_avg,"total avg")

print(even_count,"count of even")
print("count of odd",odd_count)

total_count=even_count+odd_count
print(total_count,"is total count of list")

