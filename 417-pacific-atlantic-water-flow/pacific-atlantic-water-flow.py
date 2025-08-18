class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        from collections import deque
        p_set = set()
        for i in range(rows):
            p_set.add((i,0))
        for j in range(1,cols):
            p_set.add((0,j))
        a_set = set()
        for i in range(rows):
            a_set.add((i,cols-1))
        for j in range(cols):
            a_set.add((rows-1,j))
        
        p_q = deque([[i,j] for i,j in p_set])
        a_q = deque([[i,j] for i,j in a_set])

        while p_q:
            for _ in range(len(p_q)):
                i,j = p_q.popleft()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x, y = i+dx, j+dy
                    if x >=0 and y >=0 and x <rows and y <cols and (x,y) not in p_set:
                        if heights[x][y] >= heights[i][j]:
                            p_q.append([x,y])
                            p_set.add((x,y))

        while a_q:
            for _ in range(len(a_q)):
                i,j = a_q.popleft()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x, y = i+dx, j+dy
                    if x >=0 and y >=0 and x <rows and y <cols and (x,y) not in a_set:
                        if heights[x][y] >= heights[i][j]:
                            a_q.append([x,y])
                            a_set.add((x,y))
        
        
        return [[x,y] for x,y in a_set.intersection(p_set)]