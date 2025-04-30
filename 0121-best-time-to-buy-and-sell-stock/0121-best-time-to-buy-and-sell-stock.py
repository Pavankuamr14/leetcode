class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initally we will buy an stoke and update it when we find an min price stoke
        assumeMinStock=float(inf)
        Ls=[]
        for i in range(len(prices)):
            if assumeMinStock>prices[i]:
                assumeMinStock=prices[i]
            else:
                diff=prices[i]-assumeMinStock
                Ls.append(diff)
        return max(Ls,default=0)


        # min_val=min(prices)
        # day=prices.index(min_val)
        # store=max(prices[day:])
        # return store-min_val
        

   