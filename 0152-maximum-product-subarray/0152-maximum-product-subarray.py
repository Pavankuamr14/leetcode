class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = float('-inf')
        prefixProd = 1
        suffixProd = 1
        for i in range(len(nums)):
            if prefixProd == 0:
                prefixProd =1
            if suffixProd == 0:
                suffixProd =1
            prefixProd  = prefixProd * nums[i]
            suffixProd  = suffixProd * nums[n-i-1]
            max_ = max(max_,max(prefixProd,suffixProd))
        return max_

            