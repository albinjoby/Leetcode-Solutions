class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if not res or Counter(res[-1]) != Counter(word):
                res.append(word) 

        return res