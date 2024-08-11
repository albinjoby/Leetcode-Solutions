class Solution(object):
    def maxOperations(self, nums, k):

        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        count = 0
        for i in nums:
            pair = k - i
            if pair in dic and dic[pair] > 0 and dic[i] > 0:
                if i == pair and dic[i] < 2:
                    continue
                dic[i] -= 1
                dic[pair] -= 1
                count += 1 

        return count