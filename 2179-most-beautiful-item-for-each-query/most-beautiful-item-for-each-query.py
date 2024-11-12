from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q,i) for i,q in enumerate(queries)])
        
        res = [0] * len(queries)
        max_beauty = 0
        j = 0
        for q,i in queries:
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1

            res[i] = max_beauty

        return res