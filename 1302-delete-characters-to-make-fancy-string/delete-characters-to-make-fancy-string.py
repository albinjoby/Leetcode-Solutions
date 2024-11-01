class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for letter in s:
            if len(stack) > 1 and stack[-1] == letter and stack[-2] == letter:
                continue
            else:
                stack.append(letter)


        return ''.join(stack)