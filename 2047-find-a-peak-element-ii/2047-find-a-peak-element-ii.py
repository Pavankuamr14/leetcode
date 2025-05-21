class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def maxElement(mat, rows, col):
            max_row = 0
            for i in range(1, rows):
                if mat[i][col] > mat[max_row][col]:
                    max_row = i
            return max_row

        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2
            row = maxElement(mat, n, mid)

            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]
