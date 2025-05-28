class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        MaxValue = max(piles)
        def mainLogic(piles,k,h):
            currHours = 0
            for i in range(len(piles)):
                currHours += ceil(piles[i]/k)
            return currHours
        low = 1
        high = MaxValue
        answer = high
        while low<=high:
            mid = (low + high)//2
            currHours = mainLogic(piles,mid,h)
            if currHours <= h:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
            