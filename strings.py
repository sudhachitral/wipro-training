#1
s="Krishna is Everywhere ans he is Everything"
u=0
l=0
for  i in range(len(s)):
    if s[i].islower():
        l+=1
    elif s[i].isupper():
        u+=1
print(l,u)

#2
s1='madam'

if s1[::-1]==s1:
    print("palindrome")
else:
    print("not a palindrome")
    
#3
stri="ramayya"
n=len(stri)
a=stri[:3]*n
print(a)

#4
st1="xHIx"
if st1[0]=='x' and st1[-1]=='x':
    st1=st1.removeprefix('x')
    st1=st1.removesuffix('x')
print(st1)

#5

e="wipro"
n1=3
for i in range(n1):
    print(e[-3:],end="")


#5rgdh
l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)