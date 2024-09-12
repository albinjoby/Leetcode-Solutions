class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)
        for word in words:
            word = set(word)
            if all(letter in allowed for letter in word):
                count += 1

        return count