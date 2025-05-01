class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpTable = [[-1 for _ in range(n)] for _ in range(m)]

        def countPaths(i, j, m, n, dpTable):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if dpTable[i][j] != -1:
                return dpTable[i][j]

            dpTable[i][j] = countPaths(i + 1, j, m, n, dpTable) + countPaths(i, j + 1, m, n, dpTable)
            return dpTable[i][j]

        return countPaths(0, 0, m, n, dpTable)
