class Solution:
    def compressedString(self, word: str) -> str:
        res = ''
        i = 0

        while i < len(word):
            count = 1
            while i < len(word)-1 and word[i] == word[i+1]:
                count += 1
                i += 1
            while count:
                if count >= 9:
                    res = res + str(9) + word[i]
                    count -= 9
                else:
                    res = res + str(count) + word[i]
                    count = 0
            i += 1

        return res