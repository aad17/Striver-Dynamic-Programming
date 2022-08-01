class Solution:
    def numSubseq(self, nums, k: int) -> int:
        # def recurse(idx, target, nums):
        #     # print(idx, target)
        #     if target == 0:
        #         return 1
        #     if idx == 0:
        #         return 1 if nums[0] == target else 0
        #     not_pick = recurse(idx-1, target, nums)
        #     pick = 0
        #     if target >= nums[idx]:
        #         pick = recurse(idx-1, target-nums[idx], nums)
        #     return pick + not_pick

        # print(recurse(len(nums)-1, k, nums))

        # memo = {}
        # def memoise(idx, target, nums, memo):
        #     if target == 0:
        #         return 1
        #     if idx == 0:
        #         return 1 if nums[0] == target else 0
        #     if (idx, target) in memo:
        #         return memo[(idx, target)]
        #     not_pick = memoise(idx-1, target, nums, memo)
        #     pick = 0
        #     if target >= nums[idx]:
        #         pick = memoise(idx-1, target-nums[idx], nums, memo)
        #     memo[(idx, target)] = pick + not_pick
        #     return memo[(idx, target)]

        # print(memoise(len(nums)-1, k, nums, memo))

        n = len(nums)
        def tabule(tar, dp):
            for i in range(n):
                dp[i][0] = 1
            if nums[0] <= tar:
                dp[0][nums[0]] = 1
            for idx in range(1, n):
                for target in range(tar+1):
                    not_take = dp[idx-1][target]
                    take = 0
                    if nums[idx] <= target:
                        take = dp[idx-1][target-nums[idx]]
                    dp[idx][target] = take + not_take

            return dp[n-1][k]

        dp = [[0 for _ in range(k+1)]for _ in range(n)]
        print(tabule(k, dp))


s = Solution()
print(s.numSubseq([12, 1, 3], 4))