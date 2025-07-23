class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    print(seen) 
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        return res