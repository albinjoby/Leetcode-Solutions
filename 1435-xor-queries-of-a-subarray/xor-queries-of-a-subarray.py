class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] = arr[i-1]^arr[i]

        print(arr)

        res = []
        for query in queries:
            left,right = query[0],query[1]
            if left == 0:
                res.append(arr[right])
            else:
                res.append(arr[right]^arr[left-1])

        return res