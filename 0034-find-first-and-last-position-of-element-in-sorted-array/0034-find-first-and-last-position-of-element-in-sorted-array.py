class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.SearchFirstElement(nums,target),self.SearchLastElement(nums,target)]
    
    def SearchFirstElement(self,nums,target):
        low = 0
        high = len(nums)-1
        firstElement = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                firstElement = mid
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return firstElement

    def SearchLastElement(self,nums,target):
        low = 0
        high = len(nums)-1
        LastElement  = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                LastElement = mid
                low = mid+1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return LastElement

    