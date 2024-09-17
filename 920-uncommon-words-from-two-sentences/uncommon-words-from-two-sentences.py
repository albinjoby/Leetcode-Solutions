class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        for letter in s1:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        for letter in s2:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        res = []
        for letter in dic:
            if dic[letter] == 1:
                res.append(letter)
        
        return res