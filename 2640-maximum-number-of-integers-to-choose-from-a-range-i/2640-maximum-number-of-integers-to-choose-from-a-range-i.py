class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        res,sumvalue,curr,=0,0,1
        while curr<=n:
            if curr not in banned:
                if sumvalue+curr<=maxSum:
                    res+=1
                    sumvalue+=curr
                else:
                    break
            curr+=1
        return res
       