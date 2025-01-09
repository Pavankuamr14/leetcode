class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pre=len(pref)
        count=0
        for word in words:
            if pref == word[:pre]:
                count+=1
        return count

        