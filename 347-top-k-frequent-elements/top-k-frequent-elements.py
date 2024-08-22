class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        res = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num,cnt in count.items():
            res[cnt].append(num)
        
        lst = []
        for i in range(len(res)-1,0,-1):
            for n in res[i]:
                lst.append(n)
                if len(lst) == k:
                    return lst
        
        return lst