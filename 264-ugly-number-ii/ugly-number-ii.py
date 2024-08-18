class Solution(object):
    def nthUglyNumber(self, n):
        ugly = []
        for a in range(32):
            for b in range(20):
                for c in range(14):
                    ugly.append(2**a * 3**b * 5**c)
        ugly.sort()
        return ugly[n-1]