class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for c in s:
            if c.isalnum():
                word.append(c.lower())
            
        s = ''.join(word)
        return s == s[::-1]