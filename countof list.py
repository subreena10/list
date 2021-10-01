numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
list_length=len(numbers)
more_than20=0
less_than40=0
count=0
while count<list_length:
    num=numbers[count]
    if num>20:
        more_than20=more_than20+1
    else:
        less_than40=less_than40+1
    count=count+1
print("numbers more than 20: ",more_than20)
print("numbers less than 40: ",less_than40)

