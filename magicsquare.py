magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sum=0
while i<len(magic_square):
    j=0
    while j<len(magic_square[i]):
        sum=sum+magic_square[i][j]
        j=j+1
    i=i+1
print(sum)
a=0
sum1=0
while a<len(magic_square):
    b=0
    while b<len(magic_square[a]):
        sum1=sum1+magic_square[a][b]
        b=b+1
    a=a+1
print(sum1)
c=0
d=c
sum3=0
while c<len(magic_square):
    sum3=sum3+magic_square[c][d]
    c=c+1
print(sum3)
