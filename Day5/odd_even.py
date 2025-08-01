
l=[input1,input2,input3,input4,input5]
        c=0
        if input6=='odd':
            for i in range(len(l)):
                if l[i]%2!=0:
                    c+=1
            return c
        elif input6=='even':
            for i in range(len(l)):
                if l[i]%2==0:
                    c+=1
            return c
                        
