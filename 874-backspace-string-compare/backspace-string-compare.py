class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(string):
            stack = []
            string = list(string)
            for letter in string:
                if letter == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(letter)
            return stack

        return check(s)==check(t)