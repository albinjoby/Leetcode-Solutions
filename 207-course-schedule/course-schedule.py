class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        from collections import defaultdict
        dic = defaultdict(list)

        for u,v in prerequisites:
            dic[u].append(v)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            if state == visiting:
                return False
            states[node] = visiting
            for val in dic[node]:
                if not dfs(val):
                    return False
            states[node] = visited
            return True

        for course in prerequisites:
            if not dfs(course[0]):
                return False
        
        return True