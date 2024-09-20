class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        res = 0
        negative = False
        i = 0

        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1

            if not negative and res >= 2**31:
                return 2**31 -1
            if negative and res > 2**31:
                return -2**31

        if negative:
            res = -res

        return res