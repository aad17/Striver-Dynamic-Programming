class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        def recurse(row, col):
            if row == 0 and col == 0 and obstacleGrid[0][0] != 1:
                return 1
            if row < 0 or col < 0:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            # up
            up = recurse(row-1, col)
            # left
            left = recurse(row, col-1)

            return up + left
        
        print(recurse(m-1, n-1))

        def memoise(row, col, dp):
            if row == 0 and col == 0 and obstacleGrid[0][0] != 1:
                return 1
            if row < 0 or col < 0:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            up = memoise(row-1, col, dp)
            # left
            left = memoise(row, col-1, dp)
            dp[row][col] = up + left
            return dp[row][col]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        print(memoise(m-1, n-1, dp))

        def tabule(row, col):
            for i in range(row):
                for j in range(col):
                    if obstacleGrid[row][col] == 1:
                        dp[i][j] = 0
                    elif i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        up, left = 0, 0
                        if i > 0:
                            up = dp[i-1][j]
                        if j > 0:
                            left = dp[i][j-1]
                        dp[i][j] = up + left

            return dp[row-1][col-1]          

        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        print(tabule(m-1, n-1))
                    

s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))