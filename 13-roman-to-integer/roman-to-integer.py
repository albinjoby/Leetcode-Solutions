class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "I" and i+1 < len(s) and (s[i+1] == "V" or s[i+1] == "X"):
                res -= dic[s[i]]
            elif s[i] == "X" and i+1 < len(s) and (s[i+1] == "L" or s[i+1] == "C"):
                res -= dic[s[i]]
            elif s[i] == "C" and i+1 < len(s) and (s[i+1] == "D" or s[i+1] == "M"):
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        
        return res