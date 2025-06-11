class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0]
        self.total = 0
        for i in range(len(nums)):
            self.total += nums[i]
            self.dp.append(self.total)

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1] - self.dp[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)