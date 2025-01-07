class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []

        for i in range(n):
            for j in range(n):
                if i != j and words[j].find(words[i]) != -1:
                    ans.append(words[i])
                    break

        return ans
        # s = ' '.join(words)
        # res = []
        # for w in words:
        #     if s.count(w) > 1:
        #         res.append(w)
        # return res
        # edge case that you will have that are 
        # if words list is like words=["leetcode", "solution", "des"] then ?
        # if words list is like words=["abc", "zzza", "bczzz"] then ? we will fail to met the condition.
        