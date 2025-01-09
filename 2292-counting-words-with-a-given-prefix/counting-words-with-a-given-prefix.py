class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        L = len(pref)
        count = 0
        for word in words:
            if word[:L] == pref:
                count += 1
        
        return count