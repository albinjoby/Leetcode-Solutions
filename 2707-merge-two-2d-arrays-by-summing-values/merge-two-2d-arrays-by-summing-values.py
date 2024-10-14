class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p,q = 0,0
        res = []
        while p < len(nums1) and q < len(nums2):
            if nums1[p][0] == nums2[q][0]:
                sum = nums1[p][1] + nums2[q][1]
                res.append([nums1[p][0], sum])
                p += 1
                q += 1
            elif nums1[p][0] < nums2[q][0]:
                res.append(nums1[p])
                p += 1
            else:
                res.append(nums2[q])
                q += 1

        while p < len(nums1):
            res.append(nums1[p])
            p += 1

        while q < len(nums2):
            res.append(nums2[q])
            q += 1

        return res
