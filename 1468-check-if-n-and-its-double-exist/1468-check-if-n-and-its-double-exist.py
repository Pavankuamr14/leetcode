class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        holder=set()
        for num in arr:
            if num*2 in holder or num/2 in holder:
                return True
            holder.add(num)
        return False