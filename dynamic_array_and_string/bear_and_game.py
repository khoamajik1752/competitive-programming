def calc_interesting_time(n:int,times:list)->int:
  totalTime=15
  if (times[0]>totalTime):
    print(totalTime)
    return totalTime
  for i in range(n):
    if times[i] <= totalTime:
      totalTime=times[i]+15
    else:
      print(totalTime)
      return totalTime
  totalTime=90 if totalTime>90 else totalTime
  print(totalTime)
  return totalTime
n=int(input())
times=list(map(int,input().split(" ")))
calc_interesting_time(n,times)