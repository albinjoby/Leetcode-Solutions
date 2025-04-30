class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            count = 0
            while num > 0:
                num //= 10
                count += 1
            res += 1 if count % 2 == 0 else 0
        return res