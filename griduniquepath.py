class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recurse(row, col):
            if row == 0 and col == 0:
                return 1

            if row < 0 or col < 0:
                return 0

            # up
            up = recurse(row-1, col)
            # left
            left = recurse(row, col-1)

            return up + left

        # return recurse(m-1, n-1)

        def memoise(row, col, dp):
            if row == 0 and col == 0:
                return 1

            if row < 0 or col < 0:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            # up
            up = memoise(row-1, col, dp)
            # left
            left = memoise(row, col-1, dp)

            dp[row][col] = up + left

            return dp[row][col]

        dp = [[-1 for _ in range(n)]for _ in range(m)]
        return memoise(m-1, n-1, dp)

s = Solution()
print(s.uniquePaths(3, 7))