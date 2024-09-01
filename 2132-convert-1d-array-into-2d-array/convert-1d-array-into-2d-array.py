class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        start = 0
        end = n
        res = []

        while end <= len(original):
            lst = original[start:end]
            res.append(lst)
            start = end
            end += n

        return res