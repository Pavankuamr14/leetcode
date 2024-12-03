class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=''
        i=0
        for size in spaces:
            result+=s[i:size]
            result+=' '
            i=size
        result+=s[i:]
        return result
        # Tc- O(n)
        # space-O(n)

        # for i in range(len(s)):
        #     if i in spaces:
        #         result+=' '
        #     result+=s[i]
        # return result
        # O(n*2)-TC
        # O(n)space
        