name="my name is name subreena"
new_list=[]
c=" "
for i in name:
    if i==" ":
        new_list.append(c)
        c=" "
    else:
        c+=i
if c:
    new_list.append(c)
print(new_list)
