class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        rows, cols = len(board),len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        seen = set()

        def backtrack(i,j,c):
            if c == len(word):
                return True

            if not(0 <= i < rows and 0 <= j < cols ):
                return False

            if board[i][j] != word[c] or (i,j) in seen:
                return False

            seen.add((i,j))
            for x,y in directions:
                if backtrack(i+x,j+y,c+1):
                    return True
            seen.remove((i,j))
                
            return False
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False