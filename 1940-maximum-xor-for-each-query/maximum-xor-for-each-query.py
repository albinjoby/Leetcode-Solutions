class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        mask = (2**maximumBit) - 1
        res = []

        for num in reversed(nums):
            res.append(xor ^ mask)
            xor ^= num

        return res