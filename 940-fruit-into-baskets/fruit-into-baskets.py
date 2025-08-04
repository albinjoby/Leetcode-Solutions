class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        l = 0
        counter = defaultdict(int)
        res = 0
        for r in range(len(fruits)):
            # print(fruits[l],fruits[r])
            counter[fruits[r]] += 1
            # print(counter)
            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
            res = max(res,r-l+1)
        
        return res