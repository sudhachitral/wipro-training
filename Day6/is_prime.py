#check for prime
c=0
for i in range(2,input1+1):
    if input1%i==0:
        c+=1
if c<=1:
        return 2
else:
        return 1

