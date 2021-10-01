#n=['m','a','d','o','m']
n=input("Enter a string:")
string=list(n)
list=[]
i=1
while i<=len(string):
    list.append(string[-i])
    i+=1
print(list)
if list==string:
    print("palindrome.")
else:
    print(" not a palindrome")
