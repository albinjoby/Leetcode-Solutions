class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)
        print(res)
        # if len(ratings) > 1 and ratings[0] > ratings[1]:
        #     res[0] += 1
        # if len(ratings) > 1 and ratings[-1] > ratings[-2]:
        #     res[-1] += 1
        # for i in range(1,len(ratings)-1):
        #     if ratings[i-1] < ratings[i] or ratings[i] > ratings[i+1]:
        #         res[i] += 1
        # print(res)

        for i in range(1,len(ratings)):
            if ratings[i-1] < ratings[i]:
                res[i] = res[i-1] + 1

        print(res)

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)

        print(res)

        return sum(res)
