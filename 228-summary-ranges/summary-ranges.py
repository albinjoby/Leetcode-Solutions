class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        s = ''
        lst = []
        while i < len(nums):
            temp = nums[i]
            s += str(nums[i])
            while nums[i]+1 in nums:
                i += 1
            if nums[i] != temp:
                s += '->'
                s += str(nums[i])
                lst.append(s)
                s = ''
            else:
                s = ''
                lst.append(str(temp))
            i += 1

        return lst