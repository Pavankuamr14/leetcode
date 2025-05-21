class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])-1
        def bs(array,target):
            low = 0
            high = m
            while low <= high:
                mid = (low+high)//2
                if array[mid]==target:
                    return True
                elif array[mid]>target:
                    high = mid -1
                else:
                    low = mid + 1
        for row in range(n):
            if matrix[row][0]<=target and target<=matrix[row][-1]:
                if bs(matrix[row],target):
                    return True
        return False
