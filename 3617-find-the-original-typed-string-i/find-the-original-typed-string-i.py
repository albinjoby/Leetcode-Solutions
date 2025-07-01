class Solution:
    def possibleStringCount(self, words: str) -> int:
        count = 1
        seen = set()
        current = words[0]
        for word in words:
            if word in seen and word == current:
                count += 1
            else:
                seen.add(word)
                current = word
        
        return count