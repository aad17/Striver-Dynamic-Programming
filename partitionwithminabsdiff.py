class Solution:
    def minimumDifference(self, nums) -> int:
        total_sum = sum(nums)
        n = len(nums)
        k = total_sum
        def tabule(dp):
            for i in range(n):
                dp[i][0] = True
            if nums[0] < k:
                dp[0][nums[0]] = True
            for ind in range(1, n):
                for target in range(1, k+1):
                    not_take = dp[ind-1][target]
                    take = False
                    if nums[ind] <= target:
                        take = dp[ind-1][target-nums[ind]]
                    dp[ind][target] = take or not_take
            # return dp[n-1]

        dp = [[-1 for _ in range(k+1)]for _ in range(n+1)]
        # temp = tabule(dp)
        tabule(dp)
        print(dp[n-1])

        mini = float('inf')
        for s1 in range(k+1):
            if dp[n-1][s1] == True:
                mini = min(mini, abs((total_sum-s1)-s1))

        return mini

s = Solution()
print(s.minimumDifference([8, 6, 5]))