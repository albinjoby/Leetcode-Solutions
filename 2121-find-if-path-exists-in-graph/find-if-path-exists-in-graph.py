class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:    
        from collections import defaultdict
        dic = defaultdict(list)
        seen = set()
        for u,v in edges:
            dic[u].append(v)
            dic[v].append(u)
        print(dic)

        def dfs(val):
            if val == destination:
                return True
            if val in seen:
                return False
            seen.add(val)
            if val in dic:
                for item in dic[val]:
                    if dfs(item):
                        return True
            return False

        return dfs(source)