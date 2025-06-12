class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start:int ,path:List[int]):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

            return 

        backtrack(0,[])
        return res