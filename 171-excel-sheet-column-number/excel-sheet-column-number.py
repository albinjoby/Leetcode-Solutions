class Solution:
    def titleToNumber(self, val: str) -> int:
        dic = {chr(x):x-64 for x in range(65,91)}
        res = 0
        x = 0
        for i in range(len(val)-1,-1,-1):
            res += dic[val[i]] * (26**x)
            x += 1
        return res