class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 0
        letter = word[0]
        for i in range(len(word)):
            if word[i] == letter:
                count += 1
                if count == 9:
                    comp += f"{count}{word[i]}"
                    count = 0
            else:
                comp += f"{count}{letter}" if count > 0 else ""
                count = 1
                letter = word[i]

        comp += f"{count}{word[i]}" if count > 0 else ""
        
        return comp
            