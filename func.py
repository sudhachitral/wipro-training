#1
def summ(l:list()):
    s=0
    for i in range(len(l)):
       s+=l[i]
    print(s)
       
summ([1,2,3,4])

#2
def reverse(s):
    print(s[::-1])
reverse("1234r")

#3
def factt(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    return fact
r=factt(0)
print(r)
    
#4
def count(st):
    u=0
    l=0
    for i in range(len(st)):
        if st[i].isupper():
            u+=1
        elif st[i].islower():
            l+=1
    return u,l
ra=count("Jai Sri Krishna")
print(ra)

#5
def evenno(l1:list()):
    a=[]
    for i in range(len(l1)):
        if l1[i]%2==0:
            a.append(l1[i])
    print(a)
evenno([1,2,3,4,5,56,67,8])
 
#6
def primeno(no):
    c=0
    if no==0 or no==1:
        return 1
    else:
         for i in range(2,no+1):
             if no%i==0:
                 c+=1
    if c>1:
        return ("not prime number")
    else:
        return (" prime number")
result=primeno(2)
print(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        