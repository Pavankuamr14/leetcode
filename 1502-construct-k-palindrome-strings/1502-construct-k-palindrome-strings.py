class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False

        if len(s)==k:
            return True
        freq=[0]*26
        oddCount=0
        for word in s:
            freq[ord(word)-ord("a")]+=1
        for c in freq:
            if c % 2 ==1:
                oddCount+=1
        return oddCount<=k