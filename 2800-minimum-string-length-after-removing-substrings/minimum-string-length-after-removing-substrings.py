class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for letter in s:
            if letter == 'B' and stack and stack[-1] == 'A':
                stack.pop()
                continue
            if letter == 'D' and stack and stack[-1] == 'C':
                stack.pop()
                continue
            else:
                stack.append(letter)


        return len(stack)