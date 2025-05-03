class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==1:
            return nums[0]
        nums.sort()
        cnt = 1
        holder = nums[0]
        for i in range(1,len(nums)):
            currElem = nums[i]
            if currElem  == holder:
                cnt+=1
                if cnt>n//2:
                    return holder
            else:
                holder = nums[i]
                cnt=1
        
        
        
        