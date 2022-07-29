class Solution:
    def minimumTotal(self, triangle) -> int:
        m = len(triangle)
        def recurse(row, col):
            if row == m-1:
                return triangle[row][col]

            down = triangle[row][col] + recurse(row+1, col)
            down_right = triangle[row][col] + recurse(row+1, col+1)

            return min(down, down_right)

        print(recurse(0, 0))

        def memoise(row, col, dp):
            if row == m-1:
                return triangle[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            
            down = triangle[row][col] + recurse(row+1, col)
            down_right = triangle[row][col] + recurse(row+1, col+1)

            dp[row][col] = min(down, down_right)
            return dp[row][col]

        dp = []
        for i in range(m):
            temp = []
            for j in range(i+1):
                temp.append(-1)
            dp.append(temp)

        print(memoise(0, 0, dp))

        def tabule(dp):
            for j in range(m):
                dp[m-1][j] = triangle[m-1][j]

            for i in range(m-2, -1, -1):
                for j in range(i, -1, -1):
                    down = triangle[i][j] + dp[i+1][j]
                    down_right = triangle[i][j] + dp[i+1][j+1]
                    dp[i][j] = min(down, down_right)

            return dp[0][0]

        dp = []
        for i in range(m):
            temp = []
            for j in range(i+1):
                temp.append(-1)
            dp.append(temp)

        print(tabule(dp))

        def spaceopti():
            front = [0]*(m)
            for j in range(m):
                front[j] = triangle[m-1][j]

            for i in range(m-2, -1, -1):
                curr = [-1] * (i+1)
                for j in range(i, -1, -1):
                    down = triangle[i][j] + front[j]
                    down_right = triangle[i][j] + front[j+1]
                    curr[j] = min(down, down_right)

                front = curr
            
            return front[0]

        print(spaceopti())
        
s = Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])