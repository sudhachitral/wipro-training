#add item to dic
dic1={0:10,1:20}
dic1[2]=30
print(dic1)
#2
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d1.update(d2)
d1.update(d3)
print(d1)
#3
if 1 in dic1:
    print("yesss")
else:
    print("No")

#4
dicky={1:2,3:4,5:6}
for i in dicky.keys():
    print(i,"keys")
for j in dicky.values():
    print(j,"values")
for k in dicky.items():
    print(k,"items")
    
#5
d={}
for i in range(1,16):
    d[i]=i**2
print(d)

#6
dicc={1:2,3:"dhruv",4:6,8:"krishnayya"}
c=0
for i in dicc.values():
    if isinstance(i, int):
       c+=i
print(c)






dd={1:2,3:4,5:6}
c=sum(dd.values())
print(c)
    