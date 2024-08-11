class Solution(object):
    def sumOfUnique(self, nums):
        lst = Counter(nums)
        sum = 0
        for i in lst:
            if lst[i] == 1:
                sum += i

        return sum