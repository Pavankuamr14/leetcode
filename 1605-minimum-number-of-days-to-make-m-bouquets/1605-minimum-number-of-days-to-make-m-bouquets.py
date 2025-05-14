class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = -1
        if m*k > len(bloomDay):
            return -1
        else:
            low = min(bloomDay)
            high = max(bloomDay)
            while low <= high:
                mid = (low+high)//2
                if self.isPossible(bloomDay,mid,m,k):
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            return ans
            # for value in range(min(bloomDay),max(bloomDay)+1):
            #     if self.isPossible(bloomDay,value,m,k):
            #         return value
            # return -1
        
    def isPossible(self,array,value,m,k):
        cnt=0
        noOfBoq= 0
        for i in range(len(array)):
            if array[i]<=value:
                cnt+=1
            else:
                noOfBoq += cnt//k
                cnt = 0
        noOfBoq += cnt//k

        if noOfBoq >=m:
            return True
        else:
            return False

            