a=[[4,5,6],8,[1,2,3,7],12]
for i in range(len(a)):
    b=a[i]
    if type (b)is list:
        for j in range(len(b)):
            c=b[j]
            if c%2==0:
                print(c,"even")
            else:
                print(c,"odd")
    else:
        if b%2==0:
            print(b,"even")
        else:
            print(b,"even")
