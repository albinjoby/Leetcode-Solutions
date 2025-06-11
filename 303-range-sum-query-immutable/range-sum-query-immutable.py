class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = {}

    def sumRange(self, left: int, right: int) -> int:
        if (left,right+1) in self.cache:
            return self.cache[(left,right+1)]
    
        val = sum([self.nums[x] for x in range(left,right+1)])
        self.cache[(left,right+1)] = val
        return val

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)