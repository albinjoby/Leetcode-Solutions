class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        req_sum = sum(skill) // (len(skill) // 2)
        
        counter = Counter(skill)
        res = 0

        for num in skill:
            if not counter[num]:
                continue

            diff = req_sum - num
            if not counter[diff]:
                return -1

            else:
                counter[diff] -= 1
                counter[num] -= 1
                res += num * diff

        return int(res)