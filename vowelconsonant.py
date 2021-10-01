user=input("enter your string: ")#subu
vowel=['a','e','i','o','u']
char_list=list(user)#[s,u,b,u]
vcount=0
ccount=0
for i in char_list:
    if i in vowel:
        vcount=vcount+1
        print("vowel",i)
    else:
        print("consonant",i)
        ccount=ccount+1
print(vcount,"count of vowels",ccount,"count of consonants")