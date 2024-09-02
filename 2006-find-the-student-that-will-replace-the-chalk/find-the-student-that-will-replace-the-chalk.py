class Solution:
    def chalkReplacer(self, chalks: List[int], k: int) -> int:
        total = sum(chalks)
        k = k % total

        for i in range(len(chalks)):
            if chalks[i] <= k:
                k -= chalks[i]
            else:
                return i