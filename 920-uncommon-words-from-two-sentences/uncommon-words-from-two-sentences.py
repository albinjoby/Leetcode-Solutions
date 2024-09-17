class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        for letter in s1.split(' ') + s2.split(' '):
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        res = []
        for letter in dic:
            if dic[letter] == 1:
                res.append(letter)
        
        return res