#Write a function to calculate a string's weight by summing positions of alphabetic characters (a=1 to z=26), ignoring non-letters and optionally including or excluding vowels.
s='hello world'
d={}
c=0
input2=0
l=['a','e','i','o','u']
for i in range(1,27):
    d[chr(96+i)]=i
if input2==0:
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] not in l:
                c+=d[s[i]]
    print(c)
elif input2==1:
    for i in range(len(s)):
        if s[i].isalpha():
            c+=d[s[i]]
    print(c)                
        
