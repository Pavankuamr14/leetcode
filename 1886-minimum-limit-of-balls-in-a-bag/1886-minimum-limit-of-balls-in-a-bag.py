from typing import List
from math import ceil

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(max_balls):
            operations = 0
            for n in nums:
                operations += ceil(n / max_balls) - 1
                if operations > maxOperations:
                    return False
            return True

        # Binary search
        l, r = 1, max(nums)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            if can_divide(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
