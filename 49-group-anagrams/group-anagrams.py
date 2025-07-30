class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            dic[tuple(arr)].append(s)
            
        return list(dic.values())
