class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum=0
        rightSum=sum(nums)
        resultValid=0
        for i in range(len(nums)-1):
            leftSum+=nums[i]
            rightSum-=nums[i]
            if leftSum>=rightSum:
                resultValid+=1
        return resultValid