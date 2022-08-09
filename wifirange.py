class Solution:
    def wifiRange(self, N, S, X): 
        #code here
        # flag = [False] * (N)
        temp = list(S)
        for i in range(N):
            if S[i] == '1':
                temp[i] = True
                for j in range(1, X+1):
                    if i < N and i + j < N:
                        temp[i+j] = True
                    if i >= 0 and i - j >= 0:
                        temp[i-j] = True
                        
        for i in temp:
            if i == '0':
                return False
        return True

s = Solution()
print(s.wifiRange(8, '11000010', 2))