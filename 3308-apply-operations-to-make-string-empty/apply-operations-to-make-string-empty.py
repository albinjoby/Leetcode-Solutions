class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        dic = defaultdict(int)
        res = []
        max_count = 0
        for index,letter in enumerate(s):
            dic[letter] += 1
            if max_count < dic[letter]:
                res = [letter]
                max_count = dic[letter]
            elif max_count == dic[letter]:
                res.append(letter)

        return ''.join(res)