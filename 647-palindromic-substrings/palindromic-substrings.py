class Solution:
    def countSubstrings(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            l,r = i,i
            while l > -1 and r < len(s) and s[l] == s[r]:
                seen.add((l,r))
                l -= 1
                r += 1
            l,r = i,i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                seen.add((l,r))
                l -= 1
                r += 1
        print(seen)
        return len(seen)