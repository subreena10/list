numbers = [50, 40, 23, 70, 56, 12, 5,80, 10, 7]
index=0
max=numbers[index]
for i in numbers:
    if i>max:
        max=i
numbers.remove(max)
print(numbers)
second_max=numbers[index]
for i in numbers:
    if i>second_max:
        second_max=i
print(second_max)

# numbers = [50, 40, 23, 70, 56, 12, 5,80, 10, 7]
# print(max)

# list=[45,46,47,48]
# index=0
# max=list[index]
# for num in list:
#     if num>max:
#         max=num
# list.sort()
# print(list)
# print("second max",list[-2])