char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
new_char_list=[]

while i<len(char_list):
    j=0
    newchar=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j+=1
    newchar.append (char_list[i])
    newchar.append(count)
    if newchar not in new_char_list:
        new_char_list.append(newchar)
    i+=1
print(new_char_list)
# print(count)
    
