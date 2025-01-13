class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        for letter in counter:
            if counter[letter] % 2 == 0:
                counter[letter] = 2
            else:
                counter[letter] = 1

        res = 0
        for letter in counter:
            res += counter[letter]

        return res