class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        while n:
            temp = b
            b = a + b
            a = temp
            n -= 1
        return b