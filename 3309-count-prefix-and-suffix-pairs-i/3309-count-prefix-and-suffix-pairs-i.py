class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res
        
    def isPrefixAndSuffix(self, w1, w2):
        l = len(w1)
        return w1 == w2[:l] and w1 == w2[-l:]