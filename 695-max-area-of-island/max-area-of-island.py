class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0

        def dfs(r,c,count):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in seen or grid[r][c] == 0:
                return count
            seen.add((r,c))
            if grid[r][c] == 1:
                count += 1
            for x,y in directions:
                count = max(count, dfs(r+x,c+y,count))

            return count
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in seen:
                    res = max(res, dfs(i,j,0))
        
        dfs(0,0,0)
        return res