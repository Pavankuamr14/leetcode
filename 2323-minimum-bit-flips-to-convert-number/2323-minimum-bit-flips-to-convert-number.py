class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        xor = start^goal
        while xor:
            xor&=xor-1
            count+=1
        return count