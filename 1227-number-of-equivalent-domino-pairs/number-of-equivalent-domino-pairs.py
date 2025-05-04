class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter([tuple([min(domino),max(domino)]) for domino in dominoes]).values()
        return sum([(val*(val-1))//2 for val in counter if val >= 2])