elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
even_count=0
odd_count=0
avg=0
average=0
while i<len(elements):
    if (elements[i]%2)==0:
        sum1=sum1+i
        even_count=even_count+1
    else:
        odd_count=odd_count+1
        sum=sum+i
    i+=1
print(sum,"odd sum")
avg=sum/even_count
print(avg,"average of even")

print(sum1,"even sum")
average=sum1/odd_count
print(average,"avg of odd")

print(even_count,"count of even")
print("count of odd",odd_count)
