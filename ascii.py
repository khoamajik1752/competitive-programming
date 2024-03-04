def calc(text:str)->int:
  prev=97
  totalSum=0
  for i in range(len(text)):
    ascii=ord(text[i])
    if abs(ascii-prev) >=13:
      #todo
      totalSum=totalSum+ (26-abs(ascii-prev))
    else:
      totalSum+=abs(ascii-prev)
    prev=ascii
  print(totalSum)
  return totalSum

text=input()
calc(text)
