class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def conquer(arr, l, m, r):
            left, right = arr[l:m+1] , arr[m+1:r+1]
            i, j, x = 0, 0, l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[x] = left[i]
                    i += 1
                else:
                    arr[x] = right[j]
                    j += 1
                x += 1
            
            while i < len(left):
                arr[x] = left[i]
                i += 1
                x += 1
            while j < len(right):
                arr[x] = right[j]
                j += 1
                x += 1


        def divide(arr, l, r):
            if l == r:
                return arr
            
            m = ( l + r ) // 2
            divide(arr, l, m)
            divide(arr, m+1, r)
            conquer(arr, l, m, r)
            return arr
        
        return divide(nums, 0, len(nums)-1)