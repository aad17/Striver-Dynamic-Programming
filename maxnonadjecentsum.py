# Recursive
def maxSum(n, arr):
    # Write your code here.
    def recurse(idx):
        if idx == 0:
            return arr[idx]
        
        if idx < 0:
            return 0
        
        pick = arr[idx] + recurse(idx-2)
        not_pick = recurse(idx-1)

        return max(pick, not_pick)

    return recurse(n-1)

# Memoisation
def maxSum2(n, arr):
    # Write your code here.
    def memoise(idx, dp):
        if idx == 0:
            return arr[idx]

        if idx < 0:
            return 0

        if dp[idx] != -1:
            return dp[idx]

        pick = arr[idx] + memoise(idx-2, dp)
        not_pick = memoise(idx-1, dp)
        dp[idx] = max(pick, not_pick)
        return max(dp)

    dp = [-1] * (n)
    return memoise(n-1, dp)

# Tabulation
def maxSum3(n, arr):
    def tabule(idx, dp):
        dp[0] = arr[0]
        neg = 0
        for i in range(1, n):
            if i >1:
                pick = arr[i] + dp[i-2]
            else:
                pick = arr[i]
            not_pick = dp[i-1]
            dp[i] = max(pick, not_pick)
        return max(dp)
    dp = [-1]*(n)
    return tabule(n-1, dp)  

# Space Optimisation
def maxSum4(n, arr):  
    prev2, prev = 0, arr[0]
    for i in range(1, n):
        take = arr[i]
        if i > 1:
            take += prev2
        not_take = prev
        curr = max(take, not_take)
        prev2 = prev
        prev = curr

    return prev

print(maxSum(4, [2, 1, 1, 2]))
print(maxSum2(4, [2, 1, 1, 2]))