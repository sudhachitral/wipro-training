
    a = str(input1)
    l = []  
    l1 = []  

    for i in range(len(a)):
        if a[i] not in l:
            l.append(a[i])
        else:
            l1.append(a[i])

    count = 0
    for i in range(len(l)):
        if l1.count(l[i]) % 2 == 0:
            continue
        else:
            count += 1

    if count > 1:
        return 1 
    else:
        return 2 
