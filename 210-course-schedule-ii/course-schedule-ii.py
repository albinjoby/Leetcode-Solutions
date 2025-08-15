class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        from collections import defaultdict
        dic = defaultdict(set)

        for u,v in prerequisites:
            dic[u].add(v)

        res = []
        seen = set()
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node):
            if states[node] == visiting:
                return False
            if states[node] == visited:
                return True
            states[node] = visiting
            for val in dic[node]:
                if not dfs(val):
                    return False
            states[node] = visited
            res.append(node)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res