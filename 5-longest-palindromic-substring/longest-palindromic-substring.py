class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, max_val = 0, ""
        for i in range(len(s)):
            l,r  = i,i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    max_len = r-l+1
                    max_val = s[l:r+1]
                l -= 1
                r += 1
            l,r = i,i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    max_len = r-l+1
                    max_val = s[l:r+1]
                l -= 1
                r += 1

        return max_val

            