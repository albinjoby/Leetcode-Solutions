class Solution:
    def countLargestGroup(self, n: int) -> int:
        size = [0]* 37
        for num in range(1,n+1):
            if num > 9:
                num = sum([int(i) for i in str(num)])

            size[num] += 1

        return size.count(max(size))
