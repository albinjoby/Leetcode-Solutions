class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        is_vowel, is_consonant = False, False
        letters = [chr(x) for x in range(65,91)]
        letters += [chr(x) for x in range(97,123)]
        vowels = set("aeiouAEIOU")
        numbers = "0123456789"
        for w in word:
            if w in vowels:
                is_vowel = True
            elif w in letters:
                is_consonant = True
            elif w in numbers:
                continue
            else:
                return False
        
        return is_vowel == is_consonant