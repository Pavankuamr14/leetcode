import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = float('inf')
        while low <= high:
            mid = (low+high)//2
            if self.isPossible(nums,mid,threshold):
                ans = min(ans,mid)
                high = mid -1
            else:
                low = mid +1
        return ans
    
    def isPossible(self,nums,mid,target):
        cnt = 0
        for num in nums:
            cnt+=math.ceil(num/mid)
        if cnt <= target:
            return True
        return False 