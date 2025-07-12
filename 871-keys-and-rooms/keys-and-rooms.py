class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_idx = set()
        def dfs(idx):
            if idx in visited_idx:
                return
            visited_idx.add(idx)
            for item in rooms[idx]:
                if item not in visited_idx:
                    dfs(item)
                    visited_idx.add(item)
            return 
        
        dfs(0)
        return visited_idx == set(range(len(rooms)))

        