class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive
        def recurse(idx):
            if idx == 0:
                return 1
            if idx == 1:
                return 1  
            left = recurse(idx-1)
            right = recurse(idx-2)
            return left + right

        # Memoise
        def memoise(dp, n):
            if n <= 1:
                return n
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = memoise(dp, n-1) + memoise(dp, n-2)
            return dp[n]

        # Tabulation
        def tabule(n, dp):
            dp[0], dp[1] = 0, 1
            for i in range(2, n):
                dp[i] = dp[i-2] + dp[i-1]

            return dp[n]

        return recurse(n)
    
s = Solution()
print(s.climbStairs(4))