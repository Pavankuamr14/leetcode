class Solution:
    def countPrimes(self, n: int) -> int:
        count=0
        marklist=[1]*(n+1)
        for i in range(2,n+1):
            if marklist[i]==1:
                for j in range(i*i,n,i):
                    marklist[j]=0
        for i in range(2,n):
            if marklist[i]==1:
                count+=1
        return count
        

