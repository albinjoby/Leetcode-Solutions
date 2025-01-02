class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a','e','i','o','u'])
        res = []
        cnt = [0]*len(words)
        curr = 0
        for i in range(len(words)):
            word = words[i]
            if word[-1] in vowels and word[0] in vowels:
                curr += 1
            cnt[i] = curr

        for l,r in queries:
            if l == 0:
                res.append(cnt[r])
            else:
                res.append(cnt[r] - cnt[l-1])

        print(res)
        return res