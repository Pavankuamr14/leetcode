import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMax = max(piles)
        low = 1
        high = kMax
        result = high
        while low<=high:
            mid = (low+high)//2
            ans = self.result(piles,mid)
            if ans<=h:
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
    def result(self,array,i):
        total = 0
        for j in range(len(array)):
            val = math.ceil(array[j]/i)
            total+=val
        return total
        

        