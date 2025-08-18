class Solution:
    def fib(self, n: int) -> int:
        # memo = {0:0,
        #         1:1}
        # if n in memo:
        #     return memo[n]
        # memo[n] = self.fib(n-1) + self.fib(n-2)
        # return memo[n]
        
        a,b = 0,1
        for _ in range(n):
            temp = a+b
            a = b
            b = temp
        return a