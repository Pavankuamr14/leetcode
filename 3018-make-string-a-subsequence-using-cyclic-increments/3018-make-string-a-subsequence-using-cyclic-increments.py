class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        startidx=0
        str2Length=len(str2)
        for word in str1:
            if startidx < str2Length and (ord(str2[startidx])-ord(word))%26<2:
                startidx+=1
        return startidx==str2Length