class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate cumulative XOR array
        lst = [nums[0]]
        for i in range(1, len(nums)):
            lst.append(lst[i-1] ^ nums[i])

        # Maximum possible XOR value with maximumBit bits
        max_mask = (1 << maximumBit) - 1

        # Result array to store maximum XOR values
        res = []
        while lst:
            # Calculate the maximum XOR with max_mask
            max_val = lst[-1] ^ max_mask
            res.append(max_val)
            
            # Remove the last element from lst to move backward
            lst.pop()

        # Reverse result to match expected output order
        return res