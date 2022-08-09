class Solution:
    def cutRod(self, price, n):
        #code here
        # def recurse(idx, n):
        #     # if n == 0:
        #     #     return price[idx]
        #     if idx == 0:
        #         return n * price[0]
        #     not_take = 0 + recurse(idx-1, n)
        #     take = float('-inf')
        #     rod_length = idx + 1
        #     if rod_length <= n:
        #         take = price[idx] + recurse(idx, n + rod_length)
        #     return max(take, not_take)

        # print(recurse(n-1, n))

        # memo = {}
        # def memoise(idx, n):
        #     # if n == 0:
        #     #     return price[idx]
        #     if idx == 0:
        #         return n * price[0]
        #     if (idx, n) in memo:
        #         return memo[(idx, n)]
        #     not_take = 0 + memoise(idx-1, n)
        #     take = float('-inf')
        #     rod_length = idx + 1
        #     if rod_length <= n:
        #         take = price[idx] + memoise(idx, n + rod_length)
        #     memo[(idx, n)] = max(take, not_take)
        #     return memo[(idx, n)]

        # print(memoise(n-1, n))

        def tabule(dp, n):
            # for j in range(n):
            #     dp[j][0] = price[j]
            for i in range(n+1):
                dp[0][i] = n * price[0]

            for idx in range(1, n):
                for n in range(1, len(price)):
                    not_take = 0 + dp[idx-1][n]
                    take = float('-inf')
                    rod_length = idx + 1
                    if rod_length <= n:
                        take = price[idx] + dp[idx][n - rod_length]
                    dp[idx][n] = max(take, not_take)
            return dp[n-1][n]

        dp = [[0 for _ in range(n+1)]for _ in range(n)]
        print(tabule(dp, n))

s = Solution()
print(s.cutRod([2, 5, 7, 8, 10], 5))