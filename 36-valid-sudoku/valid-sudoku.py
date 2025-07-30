class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                val = board[i][j]
                if val != "." and val in seen:
                    return False
                seen.add(val)
        
        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                val = board[j][i]
                if val != "." and val in seen:
                    return False
                seen.add(val)

        starts = [
                  (0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)
                  ]

        for col,row in starts:
            seen = set()
            for i in range(col,col+3):
                for j in range(row,row+3):
                    val = board[j][i]
                    if val != "." and val in seen:
                        return False
                    seen.add(val)

        return True