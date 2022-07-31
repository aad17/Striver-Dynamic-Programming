class Solution:
    def isSubsetSum (self, N, arr, suma):
        def recurse(idx, target):
            if target == 0:
                return True

            if idx == 0:
                return arr[0] == target

            take = False
            if arr[idx] < suma:
                take = recurse(idx-1, target - arr[idx])
            not_take = recurse(idx-1, target)

            return (take or not_take)   

        print(recurse(N-1, suma))

        def memoise(idx, target, dp):
            if target == 0:
                return True

            if idx == 0:
                return arr[0] == target

            if dp[idx][target] != -1:
                return dp[idx][target]

            take = False
            if arr[idx] < target:
                take = memoise(idx-1, target - arr[idx], dp)
            not_take = memoise(idx-1, target, dp)

            dp[idx][target] = take or not_take
            return dp[idx][target]

        dp = [[-1 for _ in range(suma+1)]for _ in range(N+1)]
        print(memoise(N-1, suma, dp))


s = Solution()
print(s.isSubsetSum(6, [3, 34, 4, 12, 5, 2], 30))