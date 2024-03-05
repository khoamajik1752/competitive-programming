
def suffix_structures(t:str,s:str)->str:
  is_longer:bool=False
  is_array:bool=False
  if len(t)>len(s):
    is_longer=True
  s_words:dict={}
  for i in range(len(s)):
    if s[i] not in s_words:
      s_words[s[i]]=1
    else:
      s_words[s[i]]=s_words[s[i]]+1
  temp:str=""
  idx=0
  for word in t:
    if idx < len(s) and s[idx]==word:
      idx+=1
    if word in s_words and s_words[word]!=0:
      s_words[word]=s_words[word]-1
      temp+=word

  if len(temp)<len(s):
    print("need tree")
    return False
  elif idx ==len(s):
    is_array=False
  else:
    is_array=True
  if is_array and is_longer:
    print("both")
    return "both"
  elif is_array and not is_longer:
    print("array")
    return "array"
  else:
    print("automaton")
    return "automaton"
t=input()
s=input()
suffix_structures(t,s)