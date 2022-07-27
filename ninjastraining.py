# Recursive
def ninjaTraining(n: int, points) -> int:
    def recurse(idx, last):
        if idx == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            return maxi

        maxi = 0
        for i in range(3):
            if i != last:
                currpoints = points[idx][i] + recurse(idx-1, i)
                maxi = max(maxi, currpoints)

        return maxi

    return recurse(n-1, 3)

# Memoisation
def ninjaTraining2(n: int, points) -> int:
    def memoise(idx, last, dp):
        if idx == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            return maxi
        
        if dp[idx][last] != -1:
            return dp[idx][last]
        
        maxi = 0
        for i in range(3):
            if i != last:
                currpoints = points[idx][i] + memoise(idx-1, i, dp)
                maxi = max(maxi, currpoints)

        dp[idx][last] = maxi
        return dp[idx][last]

    dp = [[-1 for _ in range(4)]for _ in range(n)]
    return memoise(n-1, 3, dp)

# Tabulation
def ninjaTraining3(n: int, points) -> int:
    dp = [[0 for _ in range(4)]for _ in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    # maxi = 0
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for i in range(3):
                if i != last:
                    currpoints = points[day][i] + dp[day-1][i]
                    dp[day][last] = max(dp[day][last], currpoints)

    return dp[n-1][3]


print(ninjaTraining(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
print(ninjaTraining2(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
print(ninjaTraining3(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))