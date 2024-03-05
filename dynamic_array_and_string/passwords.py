import math
def calc_time(n:int,k:int,passwords:dict,correct_password:str)->int:
  max_time=0
  min_tries=1
  max_tries=0
  min_time=0
  myKeys = list(passwords.keys())
  myKeys.sort()
  for keys in myKeys:
    if keys <=len(correct_password):
      max_tries+=len(passwords[keys])
    if keys < len(correct_password):
      min_tries+=len(passwords[keys])
  max_time=(math.ceil(max_tries/k)-1)*5 + max_tries
  min_time=(math.ceil(min_tries/k)-1)*5 +min_tries
  print(min_time,max_time)  
  return (min_time,max_time)

    
      






nk=list(map(int,input().split(" ")))
n=nk[0]
k=nk[1]
passwords:dict={}
for i in range (n):
  password=input()
  if len(password) in passwords:
    passwords[len(password)].append(password)
  else:
    passwords[len(password)]=[password]
correct_password=input()
calc_time(n,k,passwords,correct_password)