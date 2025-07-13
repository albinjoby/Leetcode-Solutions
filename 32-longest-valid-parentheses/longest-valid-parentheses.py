class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = r = count = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                count = max(count, l+r)
            if r > l:
                l = r = 0
            i += 1

        l = r = 0
        i = len(s)-1
        while i > -1:
            if s[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                count = max(count, l+r)
            if l > r:
                l = r = 0
            i -= 1

        return count