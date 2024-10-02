class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        rank = 1
        dic = {}

        for num in temp:
            if not num in dic:
                dic[num] = rank
                rank += 1

        for i,num in enumerate(arr):
            arr[i] = dic[num]

        return arr