class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid=(low+high)//2
            totaldays = self.ispossible(weights,mid)
            if totaldays <= days:
                
                high = mid -1
            else:
                low = mid+1
        return low

    def ispossible(self,weights,mid):
        days = 1
        currWeight = 0
        for weight in weights:
            if currWeight+weight>mid:
                days +=1
                currWeight = weight
            else:
                currWeight+=weight
        return days


