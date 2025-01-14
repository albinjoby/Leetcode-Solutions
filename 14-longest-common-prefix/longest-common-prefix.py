class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        length = float('inf')
        for word in strs:
            length = min(length, len(word))

        for i in range(length):
            letter = word[i]
            for word in strs:
                if word[i] != letter:
                    return res
            res += letter

        return res