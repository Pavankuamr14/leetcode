class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=1<<len(nums)
        solut=[]
        for i in range(subsets):
            lst=[]
            for j in range(i):
                if i&1<<j:
                    lst.append(nums[j])
            solut.append(lst)
        return solut

