class Solution():
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in xrange(1, n):
            grid[0][i] += grid[0][i - 1]

        for j in xrange(1, m):
            grid[j][0] += grid[j - 1][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]

if __name__ == "__main__":
    print Solution().minPathSum([[0,1]
                                ,[1,0]])
    print Solution().minPathSum([[1,3,1]
                                ,[1,5,1]
                                ,[4,2,1]])

