class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        val = 1
        while val < n:
            val *= 4

        return val == n

        # if n == 1: return True
        # for i in range(2,n+1,2):
        #     x = 1 << i
        #     if x == n:
        #         return True
        
        # return False
