n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
duplicate_list=[]
for d in n:
     if d not in duplicate_list:
        duplicate_list.append(d)
print(duplicate_list)