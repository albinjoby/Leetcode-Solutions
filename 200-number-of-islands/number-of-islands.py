class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        res = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in seen or grid[r][c] == "0":
                return

            seen.add((r,c))
            for x,y in directions:
                dfs(r+x, c+y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    res += 1
                    dfs(i,j)
        return res