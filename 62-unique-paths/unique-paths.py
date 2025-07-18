class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def check(m,n):
            if (m,n) in cache or (n,m) in cache:
                if (m,n) in cache:
                    return cache[(m,n)]
                else:
                    return cache[(n,m)]
            if m == 0 or n == 0:
                return 0
            if m == 1 and n == 1:
                return 1
            cache[(m,n)] = check(m-1,n)+check(m,n-1)
            return cache[(m,n)]

        return check(m,n)