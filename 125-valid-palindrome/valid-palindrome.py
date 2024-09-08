class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''
        for i in s:
            if i.isalnum():
                r += i.lower()

        return r == r[::-1]