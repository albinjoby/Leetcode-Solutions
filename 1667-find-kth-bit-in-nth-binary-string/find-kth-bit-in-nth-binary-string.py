class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        val = ["0"]

        def convert(s):
            return ["0" if num == "1" else "1" for num in s][::-1]

        for _ in range(n):
            prev = val[:]
            val = val + ["1"] + convert(prev)  # Correct list concatenation

        return val[k-1]  # Adjust for 0-based indexing