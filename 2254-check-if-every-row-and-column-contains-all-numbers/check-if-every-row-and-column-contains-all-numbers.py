class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        total = (n*(n+1))//2
        for row in matrix:
            if sum(row) != total or len(set(row)) != len(row):
                return False

        arr = [0]*n
        for row in matrix:
            for i in range(n):
                arr[i] += row[i]

        return len(set(arr)) == 1 and arr[-1] == total


        