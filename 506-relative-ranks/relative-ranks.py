class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = deque(["Gold Medal","Silver Medal","Bronze Medal"]+
                    list(str(i) for i in range(4,len(score)+1)))
        dic = {}
        sorted_score = sorted(score,reverse=True)
        for num in sorted_score:
            dic[num] = rank.popleft()

        for i in range(len(score)):
            score[i] = str(dic[score[i]])
        
        return score