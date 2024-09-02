class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False

        for letter in set(t):
            if s.count(letter) != t.count(letter):
                return False
                
        return True
        