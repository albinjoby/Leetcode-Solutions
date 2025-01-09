class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        counter = Counter(nums)

        for key, value in counter.items():
            arr[value].append(key)

        res = []
        for num_set in reversed(arr):
            while num_set and k:
                res.append(num_set.pop())
                k -= 1

        return res