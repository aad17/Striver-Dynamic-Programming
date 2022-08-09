class Solution:
    def change(self, amount: int, coins) -> int:
        # def recurse(idx, target):
        #     if target == 0:
        #         return 1
        #     if target <= 0:
        #         return 0
        #     if idx == 0:
        #         if target % coins[0] == 0:
        #             return 1
        #         return 0
        #     not_take = recurse(idx-1, target)
        #     take = 0
        #     if coins[idx] <= target:
        #         take = recurse(idx, target-coins[idx])
        #     return take + not_take

        # print(recurse(len(coins)-1, amount))

        # memo = {}
        # def memoise(idx, target):
        #     if target == 0:
        #         return 1
        #     if target <= 0:
        #         return 0
        #     if idx == 0:
        #         if target % coins[0] == 0:
        #             return 1
        #         return 0
        #     if (idx, target) in memo:
        #         return memo[(idx, target)]

        #     not_take = memoise(idx-1, target)
        #     take = 0
        #     if coins[idx] <= target:
        #         take = memoise(idx, target-coins[idx])
        #     memo[(idx, target)] = take + not_take
        #     return memo[(idx, target)]

        # print(memoise(len(coins)-1, amount))

        def tabule(dp):
            for T in range(amount+1):
                if T % coins[0] == 0:
                    dp[0][T] = 1
                else:
                    dp[0][T] = 0
            for idx in range(1, len(coins)):
                for target in range(amount+1):
                    not_take = dp[idx-1][target]
                    take = 0
                    if coins[idx] <= target:
                        take = dp[idx][target-coins[idx]]
                    dp[idx][target] = take + not_take

            return dp[len(coins)-1][amount]
        
        dp = [[0 for _ in range(amount+1)]for _ in range(len(coins))]
        print(tabule(dp))

        def spaceopti():
            prev, curr = [0] * (amount+1), [0] * (amount+1)
            for T in range(amount+1):
                if T % coins[0] == 0:
                    prev[T] = 1
                else:
                    prev[T] = 0
            for idx in range(1, len(coins)):
                for target in range(amount+1):
                    not_take = prev[target]
                    take = 0
                    if coins[idx] <= target:
                        take = curr[target-coins[idx]]
                    curr[target] = take + not_take
                prev = curr

            return prev[amount]

        print(spaceopti())


s = Solution()
print(s.change(5,  [1, 2, 5]))