class Solution(object):
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        res = 0

        for i in range(1,len(arrays)):
            array = arrays[i]
            res = max(res,
                max_val - array[0],
                array[-1] - min_val)

            max_val = max(max_val,array[-1])
            min_val = min(min_val,array[0])

        return res