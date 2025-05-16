class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low+high)//2
            partitions = self.CounterPartitions(nums,mid)
            if partitions > k:
                low = mid+1
            else:
                high = mid-1
        return low

    def CounterPartitions(self,nums,MaxSum):
        n = len(nums)
        partitions = 1
        currSum = 0
        for i in range(n):
            if currSum + nums[i] <= MaxSum:
                currSum += nums[i]
            else:
                partitions +=1
                currSum = nums[i]
        return partitions