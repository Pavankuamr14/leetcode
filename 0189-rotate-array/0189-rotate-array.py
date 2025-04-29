class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length  # To handle cases where k > length of the list
        for i in range(k):
            nums.insert(0, nums.pop())
        # length=len(nums)-1
        # for i in range(k):
        #     nums.insert(0,nums[length])
        # if k==0:
        #     return nums
        # del nums[-k:]
        
        # return nums