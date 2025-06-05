class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = abs(arr[-1] - arr[0])
        res = []
        for i in range(1,len(arr)):
            if abs(arr[i-1] - arr[i]) < min_abs:
                min_abs = abs(arr[i-1] - arr[i])
                res = [[arr[i-1],arr[i]]]
            elif abs(arr[i-1] - arr[i]) == min_abs:
                res.append([arr[i-1],arr[i]])
            
        return res