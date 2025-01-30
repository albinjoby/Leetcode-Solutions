class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        lst = [[] for  _ in range(len(nums)+1)]

        for num,val in counter.items():
            lst[val].append(num)

        res = []
        for val in reversed(lst):
            for num in val:
                res.append(num)
                k -= 1
                if k == 0:
                    return res