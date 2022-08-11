class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def recurse(idx1, idx2):
        #     if idx1 < 0 or idx2 < 0:
        #         return 0
        #     if text1[idx1] == text2[idx2]:
        #         return 1 + recurse(idx1-1, idx2-1)
        #     else:
        #         return max(recurse(idx1-1, idx2), recurse(idx1, idx2-1))
        # print(recurse(len(text1)-1, len(text2)-1))

        # def memoise(idx1, idx2, dp):
        #     if idx1 < 0 or idx2 < 0:
        #         return 0
        #     if dp[idx1][idx2] != -1:
        #         return dp[idx1][idx2]
        #     if text1[idx1] == text2[idx2]:
        #         dp[idx1][idx2] = 1 + memoise(idx1-1, idx2-1, dp)
        #         return dp[idx1][idx2]
        #     else:
        #         dp[idx1][idx2] = max(memoise(idx1-1, idx2, dp), memoise(idx1, idx2-1, dp))
        #         return dp[idx1][idx2]
        # dp = [[-1 for _ in range(len(text2)+1)]for _ in range(len(text1)+1)]
        # print(memoise(len(text1)-1, len(text2)-1, dp))

        def tabule(dp):
            for j in range(len(text2)+1):
                dp[0][j] = 0
            for i in range(len(text1)+1):
                dp[i][0] = 0
            for idx1 in range(1, len(text1)+1):
                for idx2 in range(1, len(text2)+1):
                    if text1[idx1-1] == text2[idx2-1]:
                        dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
                    else:
                        dp[idx1][idx2] = max(dp[idx1-1][idx2], dp[idx1][idx2-1])
            return dp[len(text1)][len(text2)]

        dp = [[0 for _ in range(len(text2)+1)]for _ in range(len(text1)+1)]
        print(tabule(dp))

        def spaceopti():
            prev = [0] * (len(text2)+1)
            curr = [0] * (len(text2)+1)

            for j in range(len(text2)+1):
                prev[j] = 0
            for idx1 in range(1, len(text1)+1):
                for idx2 in range(1, len(text2)+1):
                    if text1[idx1-1] == text2[idx2-1]:
                        curr[idx2] = 1 + prev[idx2-1]
                    else:
                        curr[idx2] = max(prev[idx2], curr[idx2-1])
                prev = curr
            return prev[len(text2)]

        print(spaceopti())

s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))