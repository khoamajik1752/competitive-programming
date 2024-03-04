
def fasten(n:int,buttons:list)-> bool:
  if n==1:
    if buttons[0] != 1:
      print("NO")
      return False
    else:
      print("YES")
      return True
  counter=0
  for i in range(n):
    if buttons[i] ==0:
      counter +=1
    if counter ==2:
      print("NO")
      return False
  if counter !=1:
    print("NO")
    return False
  print("YES")
  return True

n=int(input())
buttons=list(map(int,input().split(" ")))
fasten(n,buttons)

