
def find_segments(n:int,k:int,arr:list)->list:
  counter=0
  l=1
  distinct={}
  for i in range(n):
    if arr[i] not in  distinct:
      counter+=1
    distinct[arr[i]]=i+1
    if counter ==k:
      while True:
        if distinct[arr[l-1]]!=l:
          l+=1
        else:
          break
      print(l,i+1)
      return[l,i+1]
  print(-1,-1)
  return


nk=list(map(int,input().split(" ")))
n=nk[0]
k=nk[1]
arr=list(map(int,input().split(" ")))
find_segments(n,k,arr)