class Solution:
    def minChanges(self, s: str) -> int:
        if s.count('0') == 0 or s.count('1') == 0:
            return 0

        count = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                count += 1
        
        return count