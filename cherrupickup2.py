class Solution:
    def cherryPickup(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        def recurse(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return float('-inf')
            if row == m-1:
                if col1 == col2:
                    return grid[row][col1]
                else:
                    return grid[row][col1] + grid[row][col2]
                    
            maxi = float('-inf')
            for j1 in range(-1, 2):
                for j2 in range(-1, 2):
                    value = 0
                    if j1 == j2:
                        value = grid[row][col1]
                    else:
                        value = grid[row][col1] + grid[row][col2]

                    value += recurse(row+1, col1+j1, col2+j2)
                    maxi = max(maxi, value)
            
            return maxi

        print(recurse(0, 0, n-1))

        def memoise(row, col1, col2, dp):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return float('-inf')
            if row == m-1:
                if col1 == col2:
                    return grid[row][col1]
                else:
                    return grid[row][col1] + grid[row][col2]
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]
            paths = [-1, 0, 1]
            maxi = 0
            for j1 in range(len(paths)):
                for j2 in range(len(paths)):
                    if j1 == j2:
                        maxi = max(maxi, grid[row][col1] + memoise(row+1, col1+j1, col2+j2, dp))
                    else:
                        maxi = max(maxi, grid[row][col1] + memoise(row+1, col1+j1, col2+j2, dp))
                    dp[row][col1][col2] = maxi

            return dp[row][col1][col2]

        dp = []
        for i in range(m):
            temp = []
            for j in range(n):
                for k in range(n):
                    temp.append(-1)
                dp.append(temp)

        print(memoise(0, 0, n-1, dp))

s = Solution()
s.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])