class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag:dict[int,str]={}
        counter=0
        direction=1
        for i in range(numRows):
            zigzag[i]=""
        for i in range(len(s)):
            idx=counter%numRows if direction==1 else numRows-(counter%numRows)-1
            zigzag[idx]=zigzag[idx] +s[i]
            counter+=1
            if counter ==numRows:
                direction*=-1
                counter=1
        result=""
        for i in range(numRows):
            result+=zigzag[i]

        return result