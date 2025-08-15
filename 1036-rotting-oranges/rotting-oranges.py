class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        fresh,time = 0,0
        from collections import deque
        q = deque()

        for i in range(rows):
            for j in range( cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in directions:
                    new_x, new_y = x+dx, y+dy
                    if new_x >= 0 and new_y >= 0 and new_x < rows and new_y < cols:
                        if grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            fresh -= 1
                            q.append((new_x,new_y))
            time += 1
        
        return time if fresh == 0 else -1
