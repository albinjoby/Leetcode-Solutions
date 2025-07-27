class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            i += 1
            res.append(word2[j])
            j += 1

        if i < len(word1) or j < len(word2):
            while i < len(word1):
                res.append(word1[i])
                i += 1
            while j < len(word2):
                res.append(word2[j])
                j += 1

        return "".join(res)
