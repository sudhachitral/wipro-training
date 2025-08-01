# Write a function that returns the most frequently occurring digit (0–9) across four input integers; if there's a tie, return the highest digit among them.
d = {}
a = str(input1)
b = str(input2)
c = str(input3)
e = str(input4)
t = a + b + c + e

for i in range(len(t)):
    if t[i] not in d:
        d[t[i]] = 1 
    else:
        d[t[i]] += 1

max_count = 0
p = ''

for i in d:
    if d[i] > max_count:
        max_count = d[i]
        p = i
    elif d[i] == max_count:
        if i > p:
            p = i
