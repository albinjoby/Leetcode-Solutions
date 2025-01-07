class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words = sorted(words, key=len)
        print(words)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j] and words[i] not in res:
                    res.append(words[i])
        
        return res