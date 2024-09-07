class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_num,max_count = nums[0],1
        for num in numbers:
            if nums.count(num) > max_count:
                max_count = nums.count(num)
                max_num = num

        return max_num