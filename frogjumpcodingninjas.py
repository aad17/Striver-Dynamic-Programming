# Recursive
def recurse(idx, arr):
    left, right = float('inf'), float('inf')
    if idx == 0:
        return 0
    
    left = recurse(idx-1, arr) + abs(arr[idx] - arr[idx-1])
    if idx > 1:
        right = recurse(idx-2, arr) + abs(arr[idx] - arr[idx-2])
    
    return min(left, right) 

# Memoise
def memoise(idx, arr, dp):
    left, right = float('inf'), float('inf')
    if idx == 0:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    left = memoise(idx-1, arr, dp) + abs(arr[idx] - arr[idx-1])
    if idx > 1:
        right = memoise(idx-2, arr, dp) + abs(arr[idx] - arr[idx-2])
    dp[idx] = min(left, right)
    return dp[idx]

# Tabule
def tabule(arr, dp):
    dp[0] = 0
    left, right = float('inf'), float('inf')
    for idx in range(1, len(arr)):
        left = dp[idx-1] + abs(arr[idx] - arr[idx-1])
        if idx > 1:
            right = dp[idx-2] + abs(arr[idx] - arr[idx-2])
        dp[idx] = min(left, right)
    return dp[-1]

heights = [10, 20, 30, 10]
dp = [-1] * (len(heights))
print(recurse(len(heights)-1, heights))
print(memoise(len(heights)-1, heights, dp))
print(tabule(heights, dp))