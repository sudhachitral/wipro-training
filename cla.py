#1
from sys import argv
#print("num1 is:",argv[1])
#a =argv[1]+argv[2]
#print(a)
#print(int(argv[2])**int(argv[3]))

#2
#print(argv[0])

#3
a=[]
for i in range(len(argv)):
    a.append((argv[i]))
e=list(map(lambda a :int(a)+0,a))
print(e)
    