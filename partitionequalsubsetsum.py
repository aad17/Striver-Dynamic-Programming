class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half = int(sum(nums)/2)
        def memoise(idx, target, dp):
            if target == 0:
                return True
            if idx < 0:
                return False
            if target < 0:
                return False
            if dp[idx][target] != -1:
                return dp[idx][target]
            dp[idx][target] = memoise(idx-1, target-nums[idx-1], dp) or memoise(idx-1, target, dp)

            return dp[idx][target]

        dp = [[-1 for _ in range(half+1)]for _ in range(len(nums)+1)]
        return memoise(len(nums)-1, half, dp)

s = Solution()
print(s.canPartition([1, 5, 11, 5]))