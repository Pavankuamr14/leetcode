class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        element = None
        for i in range(len(nums)):
            if cnt == 0:
                element=nums[i]
                cnt+=1
            elif cnt>0 and nums[i]!=element:
                cnt-=1
            else:
                cnt+=1 
        for i in range(len(nums)):
            if nums[i]==element:
                cnt+=1
        if cnt>len(nums)//2:
            return element
        