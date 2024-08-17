class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        def check(self,start):
            for i in range(start,len(nums2)):
                if i != start and nums2[i] > nums2[start]:
                    return nums2[i]
            return -1

        ans = []
        for i in nums1:
            ans.append(check(self,nums2.index(i)))

        return ans


