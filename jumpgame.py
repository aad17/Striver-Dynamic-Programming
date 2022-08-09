class Solution:
    def canJump(self, nums) -> bool:
        N = len(nums)
        def recurse(idx):
            if idx == N-1:
                return True
            if idx > N-1:
                return False
            if nums[idx] == 0:
                return False
            temp = False
            for i in range(1, nums[idx]+1):
                temp = temp or recurse(idx+i)
                # return temp
            return temp

        print(recurse(0))

        memo = {}
        def memoise(idx):
            if idx == N-1:
                return True
            if idx > N-1:
                return False
            if nums[idx] == 0:
                return False
            if idx in memo:
                return memo[idx]
            temp = False
            for i in range(1, nums[idx]+1):
                temp = temp or memoise(idx+i)
            if temp:
                memo[idx] = True
            else:
                memo[idx] = False
            return memo[idx]

        # dp = [[[-1, False] for _ in range(N)]for _ in range(N)]
        print(memoise(0))

        def linear():
            if N-1 == 1:
                return True

            if nums[0] == False:
                return False

            last = N-1
            for i in range(N-2, -1, -1):
                if i + nums[i] >= last:
                    last = i

            if last == 0:
                return True
            return False

        print(linear())

s = Solution()
s.canJump([2,3,1,1,4])