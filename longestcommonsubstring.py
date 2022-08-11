class Solution:
    def longestCommonSubstr(self, text1, text2, n, m):
        # code here
        def tabule(dp):
            for j in range(len(text2)+1):
                dp[0][j] = 0
            for i in range(len(text1)+1):
                dp[i][0] = 0
            ans = 0
            for idx1 in range(1, len(text1)+1):
                for idx2 in range(1, len(text2)+1):
                    if text1[idx1-1] == text2[idx2-1]:
                        dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
                        ans = max(ans, dp[idx1][idx2])
                    else:
                        dp[idx1][idx2] = 0
            return ans

        dp = [[0 for _ in range(len(text2)+1)]for _ in range(len(text1)+1)]
        print(tabule(dp))