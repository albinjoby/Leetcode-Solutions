class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:1,1:1}
        def fibo(n):
            if n in cache:
                return cache[n]
            cache[n] = fibo(n-1) + fibo(n-2)
            return cache[n]
        
        return fibo(n)