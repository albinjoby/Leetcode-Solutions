class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t) and Counter(s) == Counter(t)