class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            wrong = False
            for letter in word:
                if letter not in allowed:
                    wrong = True
            if not wrong:
                count += 1

        return count