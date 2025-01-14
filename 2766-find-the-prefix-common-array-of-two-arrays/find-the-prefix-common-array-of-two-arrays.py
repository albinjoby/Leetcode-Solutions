class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        res = []
        set_A, set_B  = set(),set()
        for i in range(len(A)):
            if A[i] == B[i]:
                count += 1
                res.append(count)
            elif A[i] in set_B and B[i] in set_A:
                count += 2
                res.append(count)
            elif A[i] in set_B or B[i] in set_A:
                count += 1
                res.append(count)
            else:
                res.append(count)
            set_A.add(A[i])
            set_B.add(B[i])

        return res