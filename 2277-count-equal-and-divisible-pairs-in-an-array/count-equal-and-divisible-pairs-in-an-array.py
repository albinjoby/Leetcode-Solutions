class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = {}
        count = 0
        for idx, num in enumerate(nums):
            if num in counter:
                for i in counter[num]:
                    print(idx, i, (idx * i) % k == 0)
                    if (idx * i) % k == 0:
                        count += 1 
                counter[num].append(idx)
            else:
                counter[num] = [idx]

        return count
   