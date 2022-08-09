def unboundedKnapsack(n, w, profit, weight):
    def recurse(idx, wgt):
        if idx == 0:
            return int(wgt/weight[0]) * profit[0]
        not_take = 0 + recurse(idx-1, wgt)
        take = 0
        if wgt >= weight[idx]:
            take = profit[idx] + recurse(idx, wgt-weight[idx])
        return max(take, not_take)

    print(recurse(n-1, w))

    memo = {}
    def memoise(idx, wgt):
        if idx == 0:
            return int(wgt/weight[0]) * profit[0]
        if (idx, wgt) in memo:
            return memo[(idx, wgt)]

        not_take = 0 + memoise(idx-1, wgt)
        take = 0
        if wgt >= weight[idx]:
            take = profit[idx] + memoise(idx, wgt-weight[idx])

        memo[(idx, wgt)] = max(take, not_take)
        return memo[(idx, wgt)]

    print(memoise(n-1, w))

    def tabule(dp):
        for wgt in range(w+1):
            dp[0][wgt] = int(wgt/weight[0]) * profit[0]
        
        for idx in range(1, n):
            for wgt in range(w+1):
                not_take = 0 + dp[idx-1][wgt]
                take = 0
                if wgt >= weight[idx]:
                    take = profit[idx] + dp[idx][wgt-weight[idx]]

                dp[idx][wgt] = max(take, not_take) 
        return dp[n-1][wgt]

    dp = [[0 for _ in range(w+1)]for _ in range(n)]
    print(tabule(dp))

    def spaceopti():
        prev, curr = [0] * (w+1), [0] * (w+1)
        for wgt in range(w+1):
            prev[wgt] = int(wgt/weight[0]) * profit[0]
        
        for idx in range(1, n):
            for wgt in range(w+1):
                not_take = 0 + prev[wgt]
                take = 0
                if wgt >= weight[idx]:
                    take = profit[idx] + curr[wgt-weight[idx]]

                curr[wgt] = max(take, not_take)

            prev = curr

        return prev[wgt]

    print(spaceopti())
        

unboundedKnapsack(3, 10, [5, 11, 13], [2, 4, 6])