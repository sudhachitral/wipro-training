a = str(input1)
l = []
l1 = []
c=0
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
    else:
        l1.append(a[i])
for j in range(len(l)):
    if l[j] not in l1:
        c+=1
return c
            
