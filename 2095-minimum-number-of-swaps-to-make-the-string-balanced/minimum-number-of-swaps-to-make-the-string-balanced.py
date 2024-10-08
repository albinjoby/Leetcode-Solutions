class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        count = 0
        for letter in s:
            if letter == '[':
                stack.append('[')
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return (count+1)//2