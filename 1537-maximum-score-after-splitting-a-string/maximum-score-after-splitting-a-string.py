class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            print(left,right)
            res = max(res,left.count('0')+right.count('1'))

        return res