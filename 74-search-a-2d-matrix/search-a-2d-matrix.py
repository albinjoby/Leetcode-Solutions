class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        
        return False