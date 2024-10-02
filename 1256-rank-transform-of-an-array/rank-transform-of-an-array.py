class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = [0] * len(arr)
        i = 0
        for num in arr:
            temp[i] = num
            i += 1

        temp.sort()
        rank = 1
        dic = {}

        for num in temp:
            if not num in dic:
                dic[num] = rank
                rank += 1

        print(dic)

        for i,num in enumerate(arr):
            arr[i] = dic[num]

        return arr