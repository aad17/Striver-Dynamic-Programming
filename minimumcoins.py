class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        def recurse(idx, target):
            if idx == 0:
                if target % coins[idx] == 0:
                    return int(target/coins[idx])
                else:
                    return float('inf')
            not_take = 0 + recurse(idx-1, target)
            take = float('inf')
            if target >= coins[idx]:
                take = 1 + recurse(idx, target-coins[idx])
            return min(take, not_take)

        print(recurse(n-1, amount))

        memo = {}
        def memoise(idx, target):
            if idx == 0:
                if target % coins[idx] == 0:
                    return int(target/coins[idx])
                else:
                    return float('inf')
            if (idx, target) in memo:
                return memo[(idx, target)]
            not_take = 0 + memoise(idx-1, target)
            take = float('inf')
            if target >= coins[idx]:
                take = 1 + memoise(idx, target-coins[idx])
            memo[(idx, target)] = min(take, not_take)
            memo[(idx, target)]

        print(memoise(n-1, amount))

        def tabule(dp):
            for j in range(amount+1):
                if j % coins[0] == 0:
                    dp[0][j] = int(j/coins[0])
                else:
                    dp[0][j] = float('inf')
                    
            for idx in range(1, n):
                for target in range(amount+1):
                    not_take = dp[idx-1][target]
                    take = float('inf')
                    if target >= coins[idx]:
                        take = 1 + dp[idx][target-coins[idx]]
            
                dp[idx][target] = min(take, not_take)
            
            return dp[n-1][amount]
        
        dp = [[0 for _ in range(amount+1)]for _ in range(n+1)]
        ans = tabule(dp)
        if ans >= float('inf'):
            return -1
        else:
            return ans

s = Solution()
s.coinChange([2, 5, 10, 1], 27)