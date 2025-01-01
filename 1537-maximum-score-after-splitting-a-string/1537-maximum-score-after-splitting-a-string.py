class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = -inf

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            
            best = max(best, zeros - ones)
            
        if s[-1] == "1":
            ones += 1
        
        return best + ones
        # output=0
        # for i in range(0,len(s)-1):
        #     result=0
        #     left=s[0:i+1]
        #     right=s[i+1:]
        #     result+=left.count('0')
        #     result+=right.count('1')
        #     output=max(output,result)
        # return output
            
                