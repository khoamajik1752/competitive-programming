import math
def vitaly_and_strings(s:str,t:str)->str:
  result=""
  for i in range(len(s)-1,-1,-1):
    temp=s[i]
    while temp<'z':
      temp=chr(ord(temp)+1)
      if(s[:i]+temp+result<t):
        print(s[:i]+temp+result)
        return result
    if s[i] =='z':
      temp='a'
    result=temp+result

  result="No such string"
  print(result)
  return result




s=input()
t=input()
vitaly_and_strings(s,t)