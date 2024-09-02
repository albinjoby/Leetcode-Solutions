class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
    
        return True
        