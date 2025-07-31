t=(1,2,3,4,5,6,7,78,89)
print(t[3])
print(t[-4])

#2
t1=(1,2,3,4)
if 2 in t:
    print("yesss")
else:
    print("no")
    
#3
l=[1,2,3,4,5]
tup=tuple(l)
print(tup)

#4
#tp=(1,2,3,4)
#print(tp.index(2))

#4
sl=[(10,20,40),(40,50,60),(70,80,90)]
a=list(sl[-1])
a[-1]=100
a=tuple(a)
sl[-1]=a
print(sl)

