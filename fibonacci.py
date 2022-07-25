# Memoisation
# TC = O(N)
# SC = O(N) + O(N)
def memoise(dp, n):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = memoise(dp, n-1) + memoise(dp, n-2)
    return dp[n]

# Tabulation
# TC = O(N)
# SC = O(N)
def tabule(n, dp):
    dp[0], dp[1] = 0, 1
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[n]

# Space Optimised
# TC = O(N)
# SC = O(1)
def spaceop(n):
    prev2, prev = 0, 1
    for i in range(2, n+1):
        curr = prev2 + prev
        prev2 = prev
        prev = curr

    return curr

n = 5
dp = [-1] * (n+1)
print(memoise(dp, n))
print(tabule(n, dp))
print(spaceop(n))