if input2=='even':
  input1=str(input1)
  c=0
  for i in range(len(input1)):
      if int(input1[i])%2==0:
          c+=int(input1[i])
  return c
elif input2=='odd':
  input1=str(input1)
  c=0
  for i in range(len(input1)):
      if int(input1[i])%2!=0:
          c+=int(input1[i])
  return c



