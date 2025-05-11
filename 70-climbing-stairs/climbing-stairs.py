class Solution:
    def climbStairs(self, n: int) -> int:
        dp1 = 0
        dp2 = 1
        while n:
            temp = dp1 + dp2
            dp1 = dp2
            dp2 = temp
            n -= 1
        return dp2