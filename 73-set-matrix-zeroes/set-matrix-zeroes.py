class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #find the zeros and their location
        zeros = set()
        for c in range(len(matrix)):
            for r in range(len(matrix[0])):
                if matrix[c][r] == 0:
                    zeros.add((c,r))

        # set boundaries
        left, right, top, bottom = -1, len(matrix[0]), -1, len(matrix)
        print(left,right,top,bottom)

        # iterating and setting values to zero
        for r,c in zeros:
            R, C = r, c
            # iterating left:
            r, c = R, C
            while c > left:
                matrix[R][c] = 0
                c -= 1
            # iterating right:
            r, c = R, C
            while c < right:
                matrix[R][c] = 0
                c += 1
            # iteraitng top:
            r, c = R, C
            while r > top:
                matrix[r][C] = 0
                r -= 1
            # iterating bottom:
            r, c = R, C
            while r < bottom:
                matrix[r][C] = 0
                r += 1

        print(matrix)
        