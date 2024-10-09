class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for letter in s:
            if letter == '(':
                stack.append(letter)
            elif letter == ")":
                if stack:
                    stack.pop()
                else:
                    count += 1

        return len(stack) + count