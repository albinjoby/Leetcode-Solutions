class Solution(object):
    def lengthOfLIS(self, nums):
        res = []
        def binary_search(res,num):
            l,r = 0,len(res)-1
            while l<=r:
                mid = (l+r)//2
                if res[mid] == num:
                    return mid
                elif res[mid] > num:
                    r = mid-1
                else:
                    l = mid+1
            return l

        for num in nums:
            if not res or res[-1] < num:
                res.append(num)
            else:
                index = binary_search(res,num)
                res[index] = num

        return len(res)