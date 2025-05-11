class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:1,1:1}
        def fibo(n):
            if n in cache:
                return cache[n]
            if n == 0 or n == 1:
                return 1 
            fib1 = fibo(n-1)
            fib2 = fibo(n-2)
            cache[n-1] = fib1
            cache[n-2] = fib2
            return fib1 + fib2
        
        return fibo(n)