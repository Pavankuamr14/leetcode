class Solution:
    def maxScore(self, s: str) -> int:
        output=0
        for i in range(0,len(s)-1):
            result=0
            left=s[0:i+1]
            right=s[i+1:]
            result+=left.count('0')
            result+=right.count('1')
            output=max(output,result)
        return output
            
                