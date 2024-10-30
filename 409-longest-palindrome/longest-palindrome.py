class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        count = 0
        odd = False
        for letter in counter:
            if counter[letter] % 2 == 0:
                count += counter[letter]
            else:
                count += counter[letter] - 1
                odd = True
        
        if odd:
            count += 1

        return count