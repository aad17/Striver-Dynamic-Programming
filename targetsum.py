class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        def recurse(idx, suma):
            if idx >= len(nums):
                if suma == target:
                    return 1
                return 0
            add = recurse(idx+1, suma+nums[idx])
            sub = recurse(idx+1, suma-nums[idx])
            return add + sub

        memo = {}
        def memoise(idx, suma):
            if idx >= len(nums):
                if suma == target:
                    return 1
                return 0
            if (idx, suma) in memo:
                return memo[(idx, suma)]
            
            add = memoise(idx+1, suma+nums[idx])
            sub = memoise(idx+1, suma-nums[idx])
            memo[(idx, suma)] = add + sub
            return memo[(idx, suma)]
        
        return recurse(len(nums), 0)

s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))