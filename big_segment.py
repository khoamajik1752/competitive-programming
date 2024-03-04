def big_segment(n:int,segments:list):
  pointer=-1
  min_val=999999999
  max_val=0
  if n==1:
    print(1)
    return 1
  for i in range(n):
    min_val=min(min_val,segments[i][0])
    max_val=max(max_val,segments[i][1])
    if pointer != -1:
      if segments[pointer-1][0]>min_val or segments[pointer-1][1]<max_val:
        pointer=-1
    if segments[i][0]<=min_val and segments[i][1]>=max_val:
      pointer=i+1
  print(pointer)
  return pointer
    





n=int(input())
segments=[]
for i in range(n):
  segments.append(list(map(int,input().split(" "))))
big_segment(n,segments)