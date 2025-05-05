class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        cnt = 0
        presum = defaultdict(int)
        presum[0] = 1 

        for num in nums:
            curr += num
            rem = curr - k
            if rem in presum:
                cnt += presum[rem]
            presum[curr] += 1  

        return cnt