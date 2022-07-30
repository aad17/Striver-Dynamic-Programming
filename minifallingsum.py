class Solution:
    def minFallingPathSum(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        # def recurse(row, col):
        #     if col < 0 or col >= n:
        #         return float('inf')
        #     if row == m-1:
        #         return matrix[row][col]

        #     down_right = matrix[row][col] + recurse(row+1, col+1)
        #     down_left = matrix[row][col] + recurse(row+1, col-1)
        #     down = matrix[row][col] + recurse(row+1, col)

        #     return min(down_right, down, down_left)

        # mini = float('inf')
        # for j in range(n):
        #     mini = min(mini, recurse(0, j))

        # print(mini)

        def memoise(row, col, dp):
            if col < 0 or col >= n:
                return float('inf')
            if row == m-1:
                return matrix[row][col]
            if dp[row][col] != -1:
                return dp[row][col]

            down_right = matrix[row][col] + memoise(row+1, col+1, dp)
            down_left = matrix[row][col] + memoise(row+1, col-1, dp)
            down = matrix[row][col] + memoise(row+1, col, dp)

            dp[row][col] = min(down_right, down, down_left)
            return dp[row][col]

        dp = [[-1 for _ in range(n)]for _ in range(m)]
        mini = float('inf')
        for j in range(n):
            mini = min(mini, memoise(0, j, dp))

        print(mini)

        def tabule(dp):
            for j in range(n):
                dp[0][j] = matrix[0][j]
            for i in range(1, m):
                for j in range(n):
                    down_right = matrix[i][j]
                    if j+1 < n:
                        down_right += dp[i-1][j+1]
                    else:
                        down_right += float('inf')
                    down_left = matrix[i][j]
                    if j-1 >= 0:
                        down_left += dp[i-1][j-1]
                    else:
                        down_left += float('inf')
                    down = matrix[i][j] + dp[i-1][j]
                    dp[i][j] = min(down_left, down, down_right)

            mini = dp[m-1][0]
            for j in range(n):
                mini = min(mini, dp[m-1][j])

            print(mini)
        
        dp = [[-1 for _ in range(n)]for _ in range(m)]
        tabule(dp)

s = Solution()
s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])