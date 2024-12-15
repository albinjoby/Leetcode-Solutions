class Solution(object):
    def containsDuplicate(self, nums):
        counter = Counter(nums)
        for num in counter:
            if counter[num] > 1:
                return True

        return False