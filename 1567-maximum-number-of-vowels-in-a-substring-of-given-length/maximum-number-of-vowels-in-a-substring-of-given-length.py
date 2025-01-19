class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = set('aeiou')
        for r in range(0,k):
            count += 1 if s[r] in vowels else 0

        l = 0
        max_count = count
        for r in range(k,len(s)):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            l += 1
            max_count = max(max_count, count)

        return max_count