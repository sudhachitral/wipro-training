#prime numbers in a specified range
   
c1=0
for i in range(input1,input2+1):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c<=1 and i>1:
        c1+=1
return c1

    
