class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        def recurse(row, col):
            if row == 0 and col == 0:
                return grid[0][0]
            if row < 0 or col < 0:
                return float('inf')
            
            up = grid[row][col] + recurse(row-1, col)
            left = grid[row][col] + recurse(row, col-1)

            return min(up, left)

        print(recurse(m-1, n-1))

        def memoise(row, col, dp):
            if row == 0 and col == 0:
                return grid[0][0]
            if row < 0 or col < 0:
                return float('inf')
            if dp[row][col] != -1:
                return dp[row][col]

            up = grid[row][col] + recurse(row-1, col)
            left = grid[row][col] + recurse(row, col-1)

            dp[row][col] = min(up, left)

            return dp[row][col]

        dp = [[-1 for _ in range(n)]for _ in range(m)]
        print(memoise(m-1, n-1, dp))

        def tabule(row, col, dp):
            for i in range(row):
                for j in range(col):
                    if i == 0 and j == 0:
                        dp[i][j] = grid[0][0]
                    else:
                        up, left = grid[i][j], grid[i][j]
                        if i > 0:
                            up += dp[i-1][j]
                        else:
                            up = 0
                        if j > 0:
                            left += dp[i][j-1]
                        else:
                            left = 0
                        dp[i][j] = min(up, left)
            return dp[row-1][col-1]
        
        dp = [[0 for _ in range(n)]for _ in range(m)]
        print(tabule(m-1, n-1, dp))
         
    
s = Solution()
s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])