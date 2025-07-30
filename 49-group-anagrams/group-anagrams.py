class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            val = tuple(sorted(s))
            if val in dic:
                dic[val].append(s)
            else:
                dic[val] = [s]
            
        return [val for val in dic.values()]
